class Reader:
    def __init__(self, last_name, first_name, middle_name, ticket_number, 
                 registration_date, reregistration_date, category, **kwargs):
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