import sys 
from model.book import Book
from model.book_catalog import BookCatalog
from model.library_system import LibrarySystem
from model.reader import Reader 
from model.reader import Student
from model.reader import Staff
from model.reader import PO_FPK
from model.reader import PPS
from datetime import datetime, timedelta
# def main():
#     #     # Создание книги
#     # book1 = Book(
#     #     code="QA123",
#     #     title="Программирование на Python",
#     #     authors=["Иван Иванов", "Мария Петрова"],
#     #     year=2023,
#     #     place="Москва",
#     #     publisher="Эксмо",
#     #     total_copies=5
#     # )

#     # print(book1)  # Вывод информации о книге

#     # # Выдача книги
#     # if book1.borrow_book():
#     #     print("Книга успешно выдана!")
#     # else:
#     #     print("Книга недоступна для выдачи.")

#     # # Возврат книги
#     # book1.return_book()
#     # print("Книга возвращена.")

#     # # Редактирование книги
#     # book1.edit_book(title="Python для начинающих", total_copies=10)
#     # print(book1)

#     # # Поиск по запросу
#     # if book1.matches_query("Python"):
#     #     print("Книга найдена по запросу.")

#     # Создаём каталог книг
#     # catalog = BookCatalog()

#     # # Добавляем книги
#     # book1 = Book("QA123", "Программирование на Python", ["Иван Иванов"], 2023, "Москва", "Эксмо", 5)
#     # book2 = Book("QA124", "Основы алгоритмов", ["Мария Петрова"], 2022, "Санкт-Петербург", "Питер", 3)

#     # catalog.add_book(book1)
#     # catalog.add_book(book2)

#     # # Список всех книг
#     # print("Список книг в каталоге:")
#     # for book in catalog.list_books():
#     #     print(book)

#     # # Поиск книги по шифру
#     # print("\nПоиск книги по шифру QA123:")
#     # found_book = catalog.search_by_code("QA123")
#     # if found_book:
#     #     print(found_book)
#     # else:
#     #     print("Книга не найдена.")

#     # # Поиск книги по названию
#     # print("\nПоиск книги по названию 'алгоритм':")
#     # found_books = catalog.search_by_title("алгоритм")
#     # for book in found_books:
#     #     print(book)

#     # # Редактирование книги
#     # print("\nРедактирование книги QA123:")
#     # catalog.edit_book("QA123", title="Python для профессионалов", total_copies=10)

#     # # Удаление книги
#     # print("\nУдаление книги QA124:")
#     # catalog.remove_book("QA124")

#     # # Список всех книг после изменений
#     # print("\nСписок книг после изменений:")
#     # for book in catalog.list_books():
#     #     print(book)

#     #     library_system = LibrarySystem()

#     # # Создаём читателей
#     # reader1 = Reader("Иванов", "Иван", "Иванович", "ST12345", "2024-01-15", "2024-12-01", "студент")
#     # reader2 = Reader("Петрова", "Мария", "Александровна", "PR67890", "2023-03-20", "2024-11-10", "ППС")

#     # # Регистрируем читателей
#     # library_system.register_reader(reader1)
#     # library_system.register_reader(reader2)

#     # # Выводим список читателей
#     # library_system.list_readers()

#     # # Обновляем информацию о читателе
#     # library_system.update_reader_info("ST12345", first_name="Алексей", category="аспирант")

#     # # Пытаемся удалить читателя с невозвращёнными книгами
#     # library_system.issue_book("ST12345", "L001", 7)
#     # library_system.delete_reader("ST12345")

#     # # Возвращаем книгу и удаляем читателя
#     # library_system.return_book("ST12345", "L001")
#     # library_system.delete_reader("ST12345")

#     # # Выводим обновленный список читателей
#     # library_system.list_readers()
#     library_system = LibrarySystem()

#     # # Создаём книги
#     book1 = Book("L001", "Война и мир", ["Л. Н. Толстой"], 1869, "Москва", "Русская классика", 6)
#     library_system.catalog["L001"] = book1

#     book2 = Book("QA123", "Программирование на Python", ["Иван Иванов"], 2023, "Москва", "Эксмо", 5)
#     library_system.catalog["QA123"] = book2

#     # # Создаём читателя
#     # reader1 = Reader("Иванов", "Иван", "Иванович", "ST12345", "2024-01-15", "2024-12-01", "студент")
#     # library_system.register_reader(reader1)

#     # # Выдаём книгу
#     # library_system.issue_book("ST12345", "L001", 3, True)

#     # # Возвращаем книгу
#     # library_system.return_book("ST12345", "L001")

#     # # Проверяем штрафы
#     # library_system.list_fines("ST12345")

#     # # Оплата штрафов
#     # library_system.pay_fine("ST12345", 40)

#     # # Проверяем штрафы после оплаты
#     # library_system.list_fines("ST12345")


#     # Регистрация студентов
#     student = Student("Иванов", "Иван", "Иванович", 1, "2024-01-01", "2024-12-31", "Информатика", "101")
#     library_system.register_reader(student)

#     # Регистрация ППС
#     pps = PPS("Петрова", "Анна", "Сергеевна", 2, "2024-01-10", "2024-12-31", 
#             "Математика", "Профессор", "Кандидат наук", "Доцент")
#     library_system.register_reader(pps)

#     # Регистрация слушателя ПО и ФПК
#     po_fpk = PO_FPK("Сидоров", "Олег", "Николаевич", 3, "2024-01-15", "2024-12-31", 
#                     "Физика", "999")
#     library_system.register_reader(po_fpk)

#     # Список зарегистрированных читателей
#     print("\nСписок читателей:")
#     library_system.list_readers()

#     # Попытка взять книги
#     library_system.issue_book(1, "L001", 5)  # Успешно для студента
#     library_system.issue_book(1, "L001", 5)  # Успешно для студента
#     library_system.issue_book(1, "L001", 5)  # Успешно для студента
#     library_system.issue_book(1, "L001", 5)  # Успешно для студента
#     library_system.issue_book(1, "L001", 5)  # Успешно для студента
#     library_system.issue_book(1, "L001", 5) 

#     library_system.issue_book(3, "QA123", days=5)  # Ошибка: PO_FPK может пользоваться только читальными залами
#     library_system.issue_book(2, "QA123", days=100)  # Успешно: PPS может взять на 90 дней

#     library_system.return_book(1, "L001")

#     library_system.request_interlibrary_loan(1, "Мастер и Маргарита")
#     # Обработка доставки
#     library_system.process_interlibrary_loan("Мастер и Маргарита")
#     # Просмотр всех межбиблиотечных абонементов
#     library_system.view_interlibrary_loans()

#     # # Возврат книги
#     library_system.return_interlibrary_loan(1, "Мастер и Маргарита")

#     # # Проверка статуса после возврата
#     library_system.view_interlibrary_loans()

#     library_system.report_lost_or_damaged_book(1, "L001", "утеряна")

#     # Просматриваем список утерянных или испорченных книг
#     library_system.view_lost_or_damaged_books()

#     library_system.list_fines(1)

#     library_system.return_book(1, "L001")
#     library_system.return_book(1, "L001")
#     library_system.pay_fine(1, 101)

#     library_system.remove_reader(1)
    


def register_reader(library_system):
    print("Регистрация нового читателя:")
    last_name = input("Фамилия: ")
    first_name = input("Имя: ")
    middle_name = input("Отчество: ")
    ticket_number = input("Номер читательского билета: ")
    category = input("Категория (student/teacher): ")

    registration_date = datetime.now().strftime('%Y-%m-%d')
    
    extra_info = {}
    if category == "student":
        extra_info["faculty"] = input("Факультет: ")
        extra_info["group"] = input("Группа: ")
        student = Student(last_name, first_name, middle_name, ticket_number, registration_date, registration_date, extra_info["faculty"], extra_info["group"])
        library_system.register_reader(student)
        print(f"Читатель {student} успешно зарегистрирован!")

    elif category == "teacher":
        extra_info["department"] = input("Кафедра: ")
        extra_info["position"] = input("Должность: ")

        teacher = PPS(last_name, first_name, middle_name, ticket_number, registration_date, registration_date, extra_info["department"], extra_info["position"],)
        library_system.register_reader(teacher)
        print(f"Читатель {teacher} успешно зарегистрирован!")


def issue_book(library_system: LibrarySystem):
    print("Выдача книги:")
    ticket_number = input("Номер читательского билета: ")
    book_code = input("Шифр книги: ")
    days = int(input("Количество дней на которое выдается книга: "))
    simulate_overdue = input("Симуляция просрочки? (yes/no): ").lower() == "yes"

    library_system.issue_book(ticket_number, book_code, days, simulate_overdue)

def return_book(library_system):
    print("Возврат книги:")
    ticket_number = input("Номер читательского билета: ")
    book_code = input("Шифр книги: ")
    library_system.return_book(ticket_number, book_code)

def pay_fine(library_system):
    print("Оплата штрафа:")
    ticket_number = input("Номер читательского билета: ")
    amount = float(input("Сумма для оплаты: "))
    library_system.pay_fine(ticket_number, amount)

def list_fines(library_system: LibrarySystem):
    print("Просмотр штрафов:")
    ticket_number = input("Номер читательского билета: ")
    library_system.list_fines(ticket_number)
    
def add_book(library_system: LibrarySystem):
    print("Добавление книги в каталог:")
    title = input("Название книги: ")
    author = input("Автор книги: ")
    book_code = input("Шифр книги: ")
    subscription_copies = int(input("Количество экземпляров по абонементу: "))
    reading_hall_copies = int(input("Количество экземпляров в читательском зале : "))
    # library_system.add_book(title, author, book_code, copies)
    year = int(input("Год выпуска"))
    place = input("Место издания")
    publisher = input("Название издания")
    price = int(input("Цена: "))
    book = Book(book_code, title, [author], year, place, publisher, subscription_copies, reading_hall_copies, price)
    library_system.add_book_to_catalog(book)

def remove_book(library_system):
    print("Удаление книги из каталога:")
    book_code = input("Шифр книги: ")
    library_system.remove_book_from_catalog(book_code)

def show_books(library_system):
    print("Просмотр доступных книг:")
    library_system.list_all_books()

def default_setup(library_system: LibrarySystem): 
    book = Book("L001", "Война и мир", ["Лев Толстой"], 2012, "Санкт-Петербург", "Эксмо", 5, 10, 250)
    library_system.add_book_to_catalog(book)
    student = Student("Пупкин", "Вася", "Пупкинович", "1", datetime.now(), datetime.now(), "АВТФ", "АВТФ-1")
    library_system.register_reader(student)

def main():
    library_system = LibrarySystem()

    while True:
        print("\n--- Главное меню ---")
        print("1. Регистрация нового читателя")
        print("2. Выдача книги")
        print("3. Возврат книги")
        print("4. Оплата штрафа")
        print("5. Просмотр штрафов")
        print("6. Добавить книгу")
        print("7. Удалить книгу")
        print("8. Просмотр доступных книг")
        print("9. Выход")

        #TODO:- Добавить МБА

        
        choice = input("Выберите действие (1-9): ")

        if choice == "1":
            register_reader(library_system)
        elif choice == "2":
            issue_book(library_system)
        elif choice == "3":
            return_book(library_system)
        elif choice == "4":
            pay_fine(library_system)
        elif choice == "5":
            list_fines(library_system)
        elif choice == "6":
            add_book(library_system)
        elif choice == "7":
            remove_book(library_system)
        elif choice == "8":
            show_books(library_system)
        elif choice == "9":
            print("Выход из программы.")
            sys.exit(0)
        elif choice == "10": 
            default_setup(library_system)
        else:
            print("Неверный выбор, попробуйте еще раз.")

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()