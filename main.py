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
import logger

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
        elif choice == "11": 
            library_system.load_from_file()
        else:
            print("Неверный выбор, попробуйте еще раз.")

if __name__ == "__main__":
    main()
