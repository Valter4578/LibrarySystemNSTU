from model.book import Book
from model.book_catalog import BookCatalog
from model.library_system import LibrarySystem
from model.reader import Reader 
from model.reader import Student
from model.reader import Staff
from model.reader import PO_FPK
from model.reader import PPS
def main():
    #     # Создание книги
    # book1 = Book(
    #     code="QA123",
    #     title="Программирование на Python",
    #     authors=["Иван Иванов", "Мария Петрова"],
    #     year=2023,
    #     place="Москва",
    #     publisher="Эксмо",
    #     total_copies=5
    # )

    # print(book1)  # Вывод информации о книге

    # # Выдача книги
    # if book1.borrow_book():
    #     print("Книга успешно выдана!")
    # else:
    #     print("Книга недоступна для выдачи.")

    # # Возврат книги
    # book1.return_book()
    # print("Книга возвращена.")

    # # Редактирование книги
    # book1.edit_book(title="Python для начинающих", total_copies=10)
    # print(book1)

    # # Поиск по запросу
    # if book1.matches_query("Python"):
    #     print("Книга найдена по запросу.")

    # Создаём каталог книг
    # catalog = BookCatalog()

    # # Добавляем книги
    # book1 = Book("QA123", "Программирование на Python", ["Иван Иванов"], 2023, "Москва", "Эксмо", 5)
    # book2 = Book("QA124", "Основы алгоритмов", ["Мария Петрова"], 2022, "Санкт-Петербург", "Питер", 3)

    # catalog.add_book(book1)
    # catalog.add_book(book2)

    # # Список всех книг
    # print("Список книг в каталоге:")
    # for book in catalog.list_books():
    #     print(book)

    # # Поиск книги по шифру
    # print("\nПоиск книги по шифру QA123:")
    # found_book = catalog.search_by_code("QA123")
    # if found_book:
    #     print(found_book)
    # else:
    #     print("Книга не найдена.")

    # # Поиск книги по названию
    # print("\nПоиск книги по названию 'алгоритм':")
    # found_books = catalog.search_by_title("алгоритм")
    # for book in found_books:
    #     print(book)

    # # Редактирование книги
    # print("\nРедактирование книги QA123:")
    # catalog.edit_book("QA123", title="Python для профессионалов", total_copies=10)

    # # Удаление книги
    # print("\nУдаление книги QA124:")
    # catalog.remove_book("QA124")

    # # Список всех книг после изменений
    # print("\nСписок книг после изменений:")
    # for book in catalog.list_books():
    #     print(book)

    #     library_system = LibrarySystem()

    # # Создаём читателей
    # reader1 = Reader("Иванов", "Иван", "Иванович", "ST12345", "2024-01-15", "2024-12-01", "студент")
    # reader2 = Reader("Петрова", "Мария", "Александровна", "PR67890", "2023-03-20", "2024-11-10", "ППС")

    # # Регистрируем читателей
    # library_system.register_reader(reader1)
    # library_system.register_reader(reader2)

    # # Выводим список читателей
    # library_system.list_readers()

    # # Обновляем информацию о читателе
    # library_system.update_reader_info("ST12345", first_name="Алексей", category="аспирант")

    # # Пытаемся удалить читателя с невозвращёнными книгами
    # library_system.issue_book("ST12345", "L001", 7)
    # library_system.delete_reader("ST12345")

    # # Возвращаем книгу и удаляем читателя
    # library_system.return_book("ST12345", "L001")
    # library_system.delete_reader("ST12345")

    # # Выводим обновленный список читателей
    # library_system.list_readers()
    library_system = LibrarySystem()

    # # Создаём книги
    book1 = Book("L001", "Война и мир", ["Л. Н. Толстой"], 1869, "Москва", "Русская классика", 6)
    library_system.catalog["L001"] = book1

    book2 = Book("QA123", "Программирование на Python", ["Иван Иванов"], 2023, "Москва", "Эксмо", 5)
    library_system.catalog["QA123"] = book2

    # # Создаём читателя
    # reader1 = Reader("Иванов", "Иван", "Иванович", "ST12345", "2024-01-15", "2024-12-01", "студент")
    # library_system.register_reader(reader1)

    # # Выдаём книгу
    # library_system.issue_book("ST12345", "L001", 3, True)

    # # Возвращаем книгу
    # library_system.return_book("ST12345", "L001")

    # # Проверяем штрафы
    # library_system.list_fines("ST12345")

    # # Оплата штрафов
    # library_system.pay_fine("ST12345", 40)

    # # Проверяем штрафы после оплаты
    # library_system.list_fines("ST12345")


    # Регистрация студентов
    student = Student("Иванов", "Иван", "Иванович", 1, "2024-01-01", "2024-12-31", "Информатика", "101")
    library_system.register_reader(student)

    # Регистрация ППС
    pps = PPS("Петрова", "Анна", "Сергеевна", 2, "2024-01-10", "2024-12-31", 
            "Математика", "Профессор", "Кандидат наук", "Доцент")
    library_system.register_reader(pps)

    # Регистрация слушателя ПО и ФПК
    po_fpk = PO_FPK("Сидоров", "Олег", "Николаевич", 3, "2024-01-15", "2024-12-31", 
                    "Физика", "999")
    library_system.register_reader(po_fpk)

    # Список зарегистрированных читателей
    print("\nСписок читателей:")
    library_system.list_readers()

    # Попытка взять книги
    library_system.issue_book(1, "L001", 5)  # Успешно для студента
    library_system.issue_book(1, "L001", 5)  # Успешно для студента
    library_system.issue_book(1, "L001", 5)  # Успешно для студента
    library_system.issue_book(1, "L001", 5)  # Успешно для студента
    library_system.issue_book(1, "L001", 5)  # Успешно для студента
    library_system.issue_book(1, "L001", 5) 

    library_system.issue_book(3, "QA123", days=5)  # Ошибка: PO_FPK может пользоваться только читальными залами
    library_system.issue_book(2, "QA123", days=100)  # Успешно: PPS может взять на 90 дней

    library_system.return_book(1, "L001")

    library_system.request_interlibrary_loan(1, "Мастер и Маргарита")
    # Обработка доставки
    library_system.process_interlibrary_loan("Мастер и Маргарита")
    # Просмотр всех межбиблиотечных абонементов
    library_system.view_interlibrary_loans()

    # # Возврат книги
    library_system.return_interlibrary_loan(1, "Мастер и Маргарита")

    # # Проверка статуса после возврата
    library_system.view_interlibrary_loans()

    library_system.report_lost_or_damaged_book(1, "L001", "утеряна")

    # Просматриваем список утерянных или испорченных книг
    library_system.view_lost_or_damaged_books()

    

if __name__ == "__main__":
    main()