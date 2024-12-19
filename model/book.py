class Book:
    def __init__(self, code, title, authors, year, place, publisher, reading_hall_copies, subscription_copies, price=100):
        """
        Инициализация книги.
        :param code: Библиотечный шифр книги (уникальный идентификатор).
        :param title: Название книги.
        :param authors: Список авторов.
        :param year: Год издания.
        :param place: Место издания.
        :param publisher: Название издательства.
        :param total_copies: Общее количество экземпляров.
        """
        self.code = code
        self.title = title
        self.authors = authors
        self.year = year
        self.place = place
        self.publisher = publisher
        # self.total_copies = total_copies
        # self.copies_available = total_copies  # Изначально доступные экземпляры равны общему количеству.
        self.price = price
        self.reading_hall_copies = reading_hall_copies
        self.subscription_copies = subscription_copies

    def borrow_book(self):
        """
        Уменьшить количество доступных экземпляров при выдаче книги.
        :return: True, если книга успешно выдана, иначе False (если экземпляров нет).
        """
        if self.copies_available > 0:
            self.copies_available -= 1
            return True
        return False

    def return_book(self):
        """
        Увеличить количество доступных экземпляров при возврате книги.
        """
        if self.copies_available < self.total_copies:
            self.copies_available += 1

    def edit_book(self, title=None, authors=None, year=None, place=None, publisher=None, total_copies=None):
        """
        Редактировать информацию о книге.
        Параметры, которые не переданы, остаются неизменными.
        """
        if title:
            self.title = title
        if authors:
            self.authors = authors
        if year:
            self.year = year
        if place:
            self.place = place
        if publisher:
            self.publisher = publisher
        if total_copies:
            # Если общее количество экземпляров изменяется, нужно пересчитать доступные экземпляры
            self.copies_available += total_copies - self.total_copies
            self.total_copies = total_copies

    def __str__(self):
        """
        Строковое представление книги для удобного отображения.
        """
        return (f"Шифр: {self.code}, Название: {self.title}, Авторы: {', '.join(self.authors)}, "
                f"Год: {self.year}, Издательство: {self.publisher}, Место издания: {self.place}, "
                f"Читальный зал: {self.reading_hall_copies} | Абонемент: {self.subscription_copies}")

    def matches_query(self, query):
        """
        Проверка, соответствует ли книга запросу (по шифру или названию).
        :param query: Строка поиска (может быть частью шифра или названия).
        :return: True, если запрос совпадает, иначе False.
        """
        return query.lower() in self.title.lower() or query.lower() in self.code.lower()