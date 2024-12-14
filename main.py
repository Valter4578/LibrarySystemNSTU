from model.book import Book
from model.book_catalog import BookCatalog

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
    catalog = BookCatalog()

    # Добавляем книги
    book1 = Book("QA123", "Программирование на Python", ["Иван Иванов"], 2023, "Москва", "Эксмо", 5)
    book2 = Book("QA124", "Основы алгоритмов", ["Мария Петрова"], 2022, "Санкт-Петербург", "Питер", 3)

    catalog.add_book(book1)
    catalog.add_book(book2)

    # Список всех книг
    print("Список книг в каталоге:")
    for book in catalog.list_books():
        print(book)

    # Поиск книги по шифру
    print("\nПоиск книги по шифру QA123:")
    found_book = catalog.search_by_code("QA123")
    if found_book:
        print(found_book)
    else:
        print("Книга не найдена.")

    # Поиск книги по названию
    print("\nПоиск книги по названию 'алгоритм':")
    found_books = catalog.search_by_title("алгоритм")
    for book in found_books:
        print(book)

    # Редактирование книги
    print("\nРедактирование книги QA123:")
    catalog.edit_book("QA123", title="Python для профессионалов", total_copies=10)

    # Удаление книги
    print("\nУдаление книги QA124:")
    catalog.remove_book("QA124")

    # Список всех книг после изменений
    print("\nСписок книг после изменений:")
    for book in catalog.list_books():
        print(book)

if __name__ == "__main__":
    main()