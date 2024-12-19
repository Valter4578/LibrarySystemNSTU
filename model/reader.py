class Reader:
    def __init__(self, last_name, first_name, middle_name, ticket_number, 
                 registration_date, reregistration_date, category,penalties=0, **kwargs):
        """
        Инициализация читателя библиотеки.
        :param last_name: Фамилия.
        :param first_name: Имя.
        :param middle_name: Отчество.
        :param ticket_number: Номер читательского билета.
        :param registration_date: Дата регистрации.
        :param reregistration_date: Дата перерегистрации.
        :param category: Категория читателя (студент, ППС, сотрудник и т.д.).
        :param kwargs: Дополнительные данные в зависимости от категории.
        """
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.ticket_number = ticket_number
        self.registration_date = registration_date
        self.reregistration_date = reregistration_date
        self.category = category
        self.penalties = penalties  
        # Дополнительные атрибуты для каждой категории
        self.extra_info = kwargs

    def update_reader_info(self, **kwargs):
        """
        Обновление информации о читателе (например, перерегистрация).
        :param kwargs: Поля для обновления (ключ-значение).
        """
        for key, value in kwargs.items():
            if key in self.__dict__:
                setattr(self, key, value)
            elif key in self.extra_info:
                self.extra_info[key] = value
            else:
                print(f"Предупреждение: поле {key} отсутствует, оно будет добавлено.")
                self.extra_info[key] = value
        print(f"Информация о читателе {self.ticket_number} обновлена.")

    def __str__(self):
        """
        Представление информации о читателе в виде строки.
        """
        base_info = (f"ФИО: {self.last_name} {self.first_name} {self.middle_name}, "
                     f"Номер билета: {self.ticket_number}, "
                     f"Дата регистрации: {self.registration_date}, "
                     f"Дата перерегистрации: {self.reregistration_date}, "
                     f"Категория: {self.category}")
        extra_info = ", ".join([f"{key}: {value}" for key, value in self.extra_info.items()])
        return f"{base_info}, {extra_info if extra_info else 'Нет дополнительных данных'}"
    

# Подкласс для студентов
class Student(Reader):
    max_books = 4  # Максимальное количество книг
    max_days = 7   # Максимальное количество дней на книгу
    def __init__(self, last_name, first_name, middle_name, ticket_number, 
                 registration_date, reregistration_date, faculty, group):
        super().__init__(last_name, first_name, middle_name, ticket_number, 
                         registration_date, reregistration_date, "Student", 
                         faculty=faculty, group=group)

    def __str__(self):
        return super().__str__()

# Подкласс для ППС (Профессорско-преподавательский состав)
class PPS(Reader):
    max_books = 10   # Максимальное количество книг
    max_days = 90   # Максимальное количество дней на книгу
    def __init__(self, last_name, first_name, middle_name, ticket_number, 
                 registration_date, reregistration_date, department, position):
        super().__init__(last_name, first_name, middle_name, ticket_number, 
                         registration_date, reregistration_date, "PPS", 
                         department=department, position=position)

    def __str__(self):
        return super().__str__()

# Подкласс для сотрудников
class Staff(Reader):
    max_books = 3  # Максимальное количество книг
    max_days = 14  # Максимальное количество дней на книгу

    def __init__(self, last_name, first_name, middle_name, ticket_number, 
                 registration_date, reregistration_date, division, position):
        super().__init__(last_name, first_name, middle_name, ticket_number, 
                         registration_date, reregistration_date, "Staff", 
                         division=division, position=position)

    def __str__(self):
        return super().__str__()

# Подкласс для слушателей ПО и ФПК
class PO_FPK(Student):
    max_books = 0  # Максимальное количество книг
    max_days = 0  # Максимальное количество дней на книгу

    def __init__(self, last_name, first_name, middle_name, ticket_number, 
                 registration_date, reregistration_date, faculty, group):
        super().__init__(last_name, first_name, middle_name, ticket_number, 
                         registration_date, reregistration_date, faculty, group)
        self.category = "PO_FPK"  # Переопределяем категорию

    def __str__(self):
        return f"{super().__str__()} (Может использовать только читальный зал)"