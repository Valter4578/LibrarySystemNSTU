class BookCatalog:
    def __init__(self):
        """
        Инициализация каталога книг (пустого списка).
        """
        self.books = []

    def add_book(self, book):
        """
        Добавление книги в каталог.
        :param book: Объект класса Book.
        :return: True, если книга успешно добавлена, иначе False (например, шифр уже существует).
        """
        if any(existing_book.code == book.code for existing_book in self.books):
            print(f"Ошибка: Книга с шифром {book.code} уже существует в каталоге.")
            return False
        self.books.append(book)
        print(f"Книга '{book.title}' добавлена в каталог.")
        return True

    def remove_book(self, code):
        """
        Удаление книги из каталога по её шифру.
        :param code: Шифр книги.
        :return: True, если книга успешно удалена, иначе False.
        """
        for book in self.books:
            if book.code == code:
                self.books.remove(book)
                print(f"Книга с шифром {code} удалена из каталога.")
                return True
        print(f"Ошибка: Книга с шифром {code} не найдена.")
        return False

    def edit_book(self, code, **kwargs):
        """
        Редактирование информации о книге.
        :param code: Шифр книги.
        :param kwargs: Поля книги, которые нужно обновить (например, title="Новое название").
        :return: True, если книга найдена и обновлена, иначе False.
        """
        for book in self.books:
            if book.code == code:
                book.edit_book(**kwargs)
                print(f"Информация о книге с шифром {code} обновлена.")
                return True
        print(f"Ошибка: Книга с шифром {code} не найдена.")
        return False

    def search_by_code(self, code):
        """
        Поиск книги по шифру.
        :param code: Шифр книги.
        :return: Объект книги, если найден, иначе None.
        """
        for book in self.books:
            if book.code == code:
                return book
        return None

    def search_by_title(self, title):
        """
        Поиск книг по названию (включая частичное совпадение).
        :param title: Название книги или его часть.
        :return: Список книг, соответствующих запросу.
        """
        return [book for book in self.books if title.lower() in book.title.lower()]

    def list_books(self):
        """
        Вывод всех книг в каталоге.
        :return: Список строк с информацией о книгах.
        """
        if not self.books:
            print("Каталог книг пуст.")
            return []
        return [str(book) for book in self.books]