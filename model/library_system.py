from datetime import datetime, timedelta

class LibrarySystem:
    def __init__(self):
        self.catalog = {}  # Словарь с каталогом книг (ключ - библиотечный шифр, значение - объект Book)
        self.readers = {}  # Словарь с читателями (ключ - номер читательского билета, значение - объект Reader)
        self.issued_books = []  # Список выданных книг (хранит записи о выдаче)
        self.fines = {}  # Словарь со штрафами (ключ - номер читательского билета, значение - список штрафов)
        self.interlibrary_loans = []  # Межбиблиотечные заказы
        self.lost_or_damaged_books = []  # Учёт утерянных/испорченных книг

    # ------------------------ 
    # ---------- Логика выдачи книг пользователям  ----------
    # ------------------------ 
    def add_book_to_catalog(self, book):
        """
        Добавление книги в каталог.
        :param book: Объект Book.
        """
        if book.code in self.catalog:
            print(f"Книга с шифром {book.code} уже есть в каталоге.")
        else:
            self.catalog[book.code] = book
            print(f"Книга '{book.title}' добавлена в каталог.")

    def return_book(self, ticket_number, book_code):
        """
        Возврат книги в библиотеку.
        :param ticket_number: Номер читательского билета.
        :param book_code: Шифр книги.
        """
        # Проверяем, зарегистрирован ли читатель
        if ticket_number not in self.readers:
            print(f"Читатель с номером билета {ticket_number} не зарегистрирован.")
            return

        # Проверяем, есть ли запись о выдаче этой книги
        for record in self.issued_books:
            if (record["reader"].ticket_number == ticket_number and
                    record["book"].code == book_code and
                    not record["returned"]):
                
                # Обновляем статус книги
                record["returned"] = True
                record["book"].copies_available += 1

                # Проверяем, есть ли просрочка
                if record["due_date"] < datetime.now():
                    overdue_days = (datetime.now() - record["due_date"]).days
                    penalty = overdue_days * 5  # Штраф, например, 5 рублей за день
                    record["reader"].penalties += penalty
                    print(f"Книга '{record['book'].title}' возвращена с просрочкой на {overdue_days} дней. "
                          f"Начислен штраф: {penalty} рублей.")
                else:
                    print(f"Книга '{record['book'].title}' успешно возвращена.")

                return

        print(f"Книга с кодом {book_code} не числится за читателем {ticket_number} или уже была возвращена.")


    def issue_book(self, ticket_number, book_code, days, simulate_overdue = False):
        """
        Выдача книги читателю 
        :param book_code: Шифр книги 
        :param days: Количество дней на которое выдается книга 
        :param simulate_overdue: Флаг, для симуляции просрочки 
        """
        if ticket_number not in self.readers:
            print(f"Читатель с номером билета {ticket_number} не зарегистрирован.")
            return

        if book_code not in self.catalog:
            print(f"Книга с кодом {book_code} отсутствует в каталоге.")
            return

        reader = self.readers[ticket_number]
        book = self.catalog[book_code]

        if book.copies_available <= 0:
            print(f"Книга '{book.title}' временно недоступна.")
            return
        
        # Проверка ограничений для категории читателя
        if hasattr(reader, "max_books") and hasattr(reader, "max_days"):
            # Проверка на возможность выдачи книг (для PO_FPK)
            if reader.max_books == 0:
                print(f"Читатель {reader.first_name} {reader.last_name} может пользоваться только читальными залами.")
                return

            # Проверка на максимальное количество книг
            borrowed_count = len([b for b in self.issued_books if b["reader"] == reader and not b["returned"]]) 
            if borrowed_count >= reader.max_books:
                print(f"Читатель {reader.first_name} {reader.last_name} не может взять больше {reader.max_books} книг.")
                return

            # Если количество дней не указано, берем ограничение из категории
            if days is None or days > reader.max_days:
                days = reader.max_days
        else:
            print("Ограничения для данной категории читателей не заданы. Операция отклонена.")
            return

        if simulate_overdue: 
            due_date = datetime.now() - timedelta(days=days)
        else: 
            due_date = datetime.now() + timedelta(days=days)

        self.issued_books.append({
            "reader": self.readers[ticket_number],
            "book": book,
            "due_date": due_date,
            "returned": False
        })

        book.copies_available -= 1
        print(f"Книга '{book.title}' выдана читателю {self.readers[ticket_number].first_name} "
              f"до {due_date.strftime('%Y-%m-%d')}.")
        

    def return_book(self, ticket_number, book_code):
        for record in self.issued_books:
            if (record["reader"].ticket_number == ticket_number and
                    record["book"].code == book_code and
                    not record["returned"]):
                record["returned"] = True
                record["book"].copies_available += 1

                # Проверяем на просрочку
                today = datetime.now()
                if today > record["due_date"]:
                    overdue_days = (today - record["due_date"]).days
                    fine = self.calculate_fine(overdue_days)
                    self.fines[ticket_number].append({
                        "book": record["book"].title,
                        "overdue_days": overdue_days,
                        "fine": fine,
                        "paid": False  # Фиксируем штраф как неоплаченный
                    })
                    print(f"Книга '{record['book'].title}' возвращена с просрочкой в {overdue_days} дней. "
                          f"Начислен штраф: {fine} условных единиц.")
                else:
                    print(f"Книга '{record['book'].title}' возвращена в срок.")
                return

        print(f"Книга с кодом {book_code} не найдена у читателя с номером билета {ticket_number}.")

    def show_issued_books(self):
        """
        Показать список всех выданных книг.
        """
        print("Список выданных книг:")
        for record in self.issued_books:
            status = "Возвращена" if record["returned"] else "На руках"
            print(f"- Книга: {record['book'].title}, Читатель: {record['reader'].first_name} "
                  f"{record['reader'].last_name}, Дата выдачи: {record['issue_date'].strftime('%Y-%m-%d')}, "
                  f"Дата возврата: {record['return_date'].strftime('%Y-%m-%d')}, Статус: {status}")
            
    # ------------------------ 
    # ---------- Логика регистрации пользователей в библиотечной системе  ----------
    # ------------------------ 
    def register_reader(self, reader):
        """
        Регистрация нового читателя в системе.
        :param reader: Объект Reader.
        """
        if reader.ticket_number in self.readers:
            print(f"Читатель с номером билета {reader.ticket_number} уже зарегистрирован.")
        else:
            self.readers[reader.ticket_number] = reader
            self.fines[reader.ticket_number] = []  # Инициализируем историю штрафов

            print(f"Читатель {reader.first_name} {reader.last_name} зарегистрирован.")

    def update_reader_info(self, ticket_number, **kwargs):
        """
        Обновление информации о читателе.
        :param ticket_number: Номер читательского билета.
        :param kwargs: Параметры для обновления (например, first_name, last_name).
        """
        if ticket_number not in self.readers:
            print(f"Читатель с номером билета {ticket_number} не найден.")
            return

        reader = self.readers[ticket_number]
        for key, value in kwargs.items():
            if hasattr(reader, key):
                setattr(reader, key, value)
                print(f"Поле '{key}' обновлено для читателя с номером {ticket_number}.")
            else:
                print(f"Поле '{key}' отсутствует у читателя.")

    def delete_reader(self, ticket_number):
        """
        Удаление читателя из системы, если он вернул все книги.
        :param ticket_number: Номер читательского билета.
        """
        if ticket_number not in self.readers:
            print(f"Читатель с номером билета {ticket_number} не найден.")
            return

        # Проверяем, есть ли у читателя выданные книги
        for record in self.issued_books:
            if record["reader"].ticket_number == ticket_number and not record["returned"]:
                print(f"Невозможно удалить читателя с номером билета {ticket_number}: "
                      f"у него есть невозвращенные книги.")
                return

        # Удаляем читателя
        del self.readers[ticket_number]
        print(f"Читатель с номером билета {ticket_number} успешно удалён.")

    def list_readers(self):
        """
        Вывод списка всех зарегистрированных читателей.
        """
        print("Список зарегистрированных читателей:")
        if not self.readers:
            print("Список пуст.")
            return

        for ticket_number, reader in self.readers.items():
            print(f"- Билет №{ticket_number}: {reader.first_name} {reader.last_name}, категория: {reader.category}")

    # ------------------------ 
    # ---------- Штрафы ----------
    # ------------------------ 
    def calculate_fine(self, overdue_days, fine_per_day=10):
        """
        Рассчитывает штраф на основе количества просроченных дней.
        :param overdue_days: Количество просроченных дней.
        :param fine_per_day: Ставка штрафа за день (по умолчанию 10 рублей).
        :return: Сумма штрафа.
        """
        return overdue_days * fine_per_day
    
    def list_fines(self, ticket_number):
        """
        Выводит историю штрафов читателя.
        """
        if ticket_number not in self.readers:
            print(f"Читатель с номером билета {ticket_number} не зарегистрирован.")
            return

        print(f"Штрафы для читателя {self.readers[ticket_number].first_name} {self.readers[ticket_number].last_name}:")
        if not self.fines[ticket_number]:
            print("Нет начисленных штрафов.")
            return

        total_fine = 0
        total_paid = 0
        for fine_record in self.fines[ticket_number]:
            status = "оплачено" if fine_record["paid"] else "не оплачено"
            print(f"- Книга: {fine_record['book']}, Просрочка: {fine_record['overdue_days']} дней, "
                  f"Штраф: {fine_record['fine']} условных единиц ({status}).")
            total_fine += fine_record["fine"]
            if fine_record["paid"]:
                total_paid += fine_record["fine"]

        print(f"Общая сумма штрафов: {total_fine} условных единиц.")
        self.readers[ticket_number].fines = total_fine - total_paid
        print(f"Осталось к оплате: {total_fine - total_paid} условных единиц.")

    def pay_fine(self, ticket_number, amount):
        """
        Оплата штрафов.
        :param ticket_number: Номер читательского билета.
        :param amount: Сумма оплаты.
        """
        if ticket_number not in self.readers:
            print(f"Читатель с номером билета {ticket_number} не зарегистрирован.")
            return

        unpaid_fines = [fine for fine in self.fines[ticket_number] if not fine["paid"]]
        if not unpaid_fines:
            print(f"Читатель {self.readers[ticket_number].first_name} {self.readers[ticket_number].last_name} "
                  f"не имеет неоплаченных штрафов.")
            return

        remaining_amount = amount
        for fine in unpaid_fines:
            if remaining_amount <= 0:
                break
            if not fine["paid"]:
                if remaining_amount >= fine["fine"]:
                    remaining_amount -= fine["fine"]
                    fine["paid"] = True
                else:
                    fine["fine"] -= remaining_amount
                    remaining_amount = 0

        if remaining_amount > 0:
            print(f"Оплата превышает сумму штрафов. Остаток {remaining_amount} условных единиц возвращён читателю.")
        else:
            print(f"Все доступные штрафы оплачены.")

    # ------------------------ 
    # ---------- МБА ----------
    # ------------------------ 
    def request_interlibrary_loan(self, ticket_number, book_title):
        """
        Создание запроса на межбиблиотечный абонемент (МБА).
        :param ticket_number: Номер читательского билета.
        :param book_title: Название книги для заказа.
        """
        # Проверяем наличие читателя
        if ticket_number not in self.readers:
            print(f"Читатель с номером билета {ticket_number} не зарегистрирован.")
            return

        # Проверяем, есть ли книга в текущем каталоге и доступна ли она
        for book in self.catalog.values():
            if book.title.lower() == book_title.lower() and book.copies_available > 0:
                print(f"Книга '{book_title}' доступна в текущей библиотеке. "
                      f"Вы можете взять её на обычных условиях.")
                return

        # Если книги нет или недостаточно, оформляем межбиблиотечный заказ
        loan = {
            "reader": self.readers[ticket_number],
            "book_title": book_title,
            "status": "В обработке",
            "due_date": None,
            "returned": False
        }
        self.interlibrary_loans.append(loan)
        print(f"Запрос на межбиблиотечный абонемент для книги '{book_title}' создан. "
              f"Статус: В обработке.")

    def process_interlibrary_loan(self, book_title):
        """
        Обработка межбиблиотечного заказа.
        :param book_title: Название книги.
        """
        for loan in self.interlibrary_loans:
            if loan["book_title"].lower() == book_title.lower() and loan["status"] == "В обработке":
                loan["status"] = "Доставлено"
                loan["due_date"] = datetime.now() + timedelta(days=30)  # Например, срок 30 дней
                print(f"Книга '{book_title}' доставлена по межбиблиотечному абонементу. "
                      f"Срок возврата: {loan['due_date'].strftime('%Y-%m-%d')}.")
                return

        print(f"Нет активных запросов на книгу '{book_title}' для обработки.")

    def return_interlibrary_loan(self, ticket_number, book_title):
        """
        Возврат книги, полученной по межбиблиотечному абонементу.
        :param ticket_number: Номер читательского билета.
        :param book_title: Название книги.
        """
        for loan in self.interlibrary_loans:
            if (loan["reader"].ticket_number == ticket_number and
                    loan["book_title"].lower() == book_title.lower() and
                    not loan["returned"]):
                loan["returned"] = True

                # Проверяем просрочку
                if loan["due_date"] < datetime.now():
                    overdue_days = (datetime.now() - loan["due_date"]).days
                    penalty = overdue_days * 10  # Штраф, например, 10 рублей за день
                    loan["reader"].penalties += penalty
                    print(f"Книга '{book_title}' возвращена с просрочкой на {overdue_days} дней. "
                          f"Начислен штраф: {penalty} рублей.")
                else:
                    print(f"Книга '{book_title}' возвращена вовремя. Спасибо!")

                loan["status"] = "Возвращено"
                return

        print(f"Нет активных запросов на книгу '{book_title}' для возврата.")

    def view_interlibrary_loans(self):
        """
        Вывод информации о всех межбиблиотечных абонементах.
        """
        if not self.interlibrary_loans:
            print("Нет активных запросов на межбиблиотечный абонемент.")
            return

        for loan in self.interlibrary_loans:
            status = loan["status"]
            due_date = loan["due_date"].strftime('%Y-%m-%d') if loan["due_date"] else "Не указана"
            returned = "Да" if loan["returned"] else "Нет"
            print(f"Книга: {loan['book_title']}, Статус: {status}, "
                  f"Срок возврата: {due_date}, Возвращена: {returned}")
            
    # ------------------------ 
    # ------ Учет испорченных книг --------
    # ------------------------ 

    def report_lost_or_damaged_book(self, ticket_number, book_code, condition):
        """
        Отчёт об утерянной или испорченной книге.
        :param ticket_number: Номер читательского билета.
        :param book_code: Код книги.
        :param condition: Состояние книги: 'утеряна' или 'испорчена'.
        """
        if ticket_number not in self.readers:
            print(f"Читатель с номером билета {ticket_number} не зарегистрирован.")
            return

        if book_code not in self.catalog:
            print(f"Книга с кодом {book_code} отсутствует в каталоге.")
            return

        # Проверяем, есть ли книга в списке выданных
        book = self.catalog[book_code]
        incidents = [
            issued for issued in self.issued_books
            if issued["reader"].ticket_number == ticket_number and issued["book"] == book and not issued["returned"]
        ]

        if not incidents:
            print(f"Книга '{book.title}' не числится как выданная этому читателю.")
            return

        # Отмечаем книгу как утерянную или испорченную
        incident = incidents[0]
        incident["returned"] = True  # Закрываем выдачу

        # Уменьшаем количество доступных копий
        book.copies_available -= 1

        # Начисляем штраф
        if condition == "утеряна":
            penalty = book.price * 10 
            status = "Утеряна"
        elif condition == "испорчена":
            penalty = book.price * 0.5
            status = "Испорчена"
        else:
            print("Ошибка: Неверное состояние книги. Укажите 'утеряна' или 'испорчена'.")
            return

        self.readers[ticket_number].fines += penalty
        self.lost_or_damaged_books.append({
            "reader": self.readers[ticket_number],
            "book": book,
            "status": status,
            "penalty": penalty,
            "date": datetime.now()
        })

        print(f"Книга '{book.title}' отмечена как {status}. Начислен штраф: {penalty} рублей.")

        # Если больше нет копий, удаляем книгу из доступного каталога
        if book.copies_available <= 0:
            print(f"Книга '{book.title}' больше недоступна в каталоге.")
            del self.catalog[book_code]

    def view_lost_or_damaged_books(self):
        """
        Просмотр всех утерянных или испорченных книг.
        """
        if not self.lost_or_damaged_books:
            print("Нет зарегистрированных случаев утери или порчи книг.")
            return

        print("Список утерянных и испорченных книг:")
        for record in self.lost_or_damaged_books:
            reader = record["reader"]
            book = record["book"]
            print(f"Читатель: {reader.first_name} {reader.last_name}, "
                  f"Книга: {book.title}, Статус: {record['status']}, "
                  f"Штраф: {record['penalty']} руб., Дата: {record['date'].strftime('%Y-%m-%d')}")