class Student:
    def __init__(self, name: str, marks: int) -> None:
        self._name = name
        self._marks = marks

    @property
    def name(self):
        return self._name

    @property
    def marks(self):
        return self._marks

    def is_passed(self) -> bool:
        return self._marks > 50

    def __str__(self) -> str:
        return f"{self._name}\n"


class Library:
    def __init__(self,
                 city: str,
                 street: str,
                 zip_code: str,
                 open_hours: str,
                 phone: str) -> None:

        self._city = city
        self._street = street
        self._zip_code = zip_code
        self._open_hours = open_hours
        self._phone = phone

    @property
    def city(self):
        return self._city

    @property
    def street(self):
        return self._street

    @property
    def zip_code(self):
        return self._zip_code

    @property
    def open_hours(self):
        return self._open_hours

    @property
    def phone(self):
        return self._phone

    def __str__(self) -> str:
        return f"""\tAdres biblioteki: \n\t\t
                    miasto: {self._city}\n\t\t
                    ulica: {self._street}\n\t\t
                    kod pocztowy: {self._zip_code}\n\t
                    Godziny otwarcia: {self._open_hours}\n\t
                    Numer telefonu:{self._phone}"""


class Order:
    def __init__(self, employee: str,
                 student: str, books: str,
                 order_date: str) -> None:
        self._employee = employee
        self._student = student
        self._books = books
        self._order_date = order_date

    @property
    def employee(self):
        return self._employee

    @property
    def student(self):
        return self._student

    @property
    def books(self):
        return self._books

    @property
    def order_date(self):
        return self._order_date

    def __str__(self) -> str:
        return f"""\nZamówienie zrealizował/a: {self._employee}\n
                Student: {self._student}\n
                Zamówiona książka: {self._books}\n
                Data zamówienia: {self._order_date}"""


class Employee:
    def __init__(self,
                 first_name: str,
                 last_name: str,
                 hire_date: str,
                 birth_date: str,
                 city: str,
                 street: str,
                 zip_code: str,
                 phone: str) -> None:

        self._first_name = first_name
        self._last_name = last_name
        self._hire_date = hire_date
        self._birth_date = birth_date
        self._city = city
        self._street = street
        self._zip_code = zip_code
        self._phone = phone

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def _hire_date(self):
        return self._hire_date

    @property
    def birth_date(self):
        return self._birth_date

    @property
    def city(self):
        return self._city

    @property
    def street(self):
        return self._street

    @property
    def zip_code(self):
        return self._zip_code

    @property
    def phone(self):
        return self._phone

    def __str__(self) -> str:
        return f"""\n\tImię pracownika: {self._first_name}\n\t
                Nazwisko pracownika: {self._last_name}\n\t
                Data zatrudnienia: {self._hire_date}\n\t
                Data urodzenia: {self._birth_date}\n\t
                Miasto: {self._city}\n\t
                Ulica: {self._street}\n\t
                Kod pocztowy: {self._zip_code}\n\t
                Numer telefonu: {self.phone}\n"""


class Book:
    def __init__(self, library: str,
                 publication_date: str,
                 author_name: str,
                 author_surname: str,
                 number_of_pages: int) -> None:
        self._library = library
        self._publication_date = publication_date
        self._author_name = author_name
        self._author_surname = author_surname
        self._number_of_pages = number_of_pages

    @property
    def library(self):
        return self._library

    @property
    def publication_date(self):
        return self._publication_date

    @property
    def author_name(self):
        return self._author_name

    @property
    def author_surname(self):
        return self._author_surname

    @property
    def number_of_pages(self):
        return self._number_of_pages

    def __str__(self) -> str:
        return f"""\n{self._library}\n
                Data publikacji: {self._publication_date}\n
                Autor/ka ksiązki: {self._author_name} {self._author_surname}\n
                Liczba stron: {self._number_of_pages}"""


student1 = Student("Jan Kowalski", 43)
student2 = Student("Zofia Has", 29)
student3 = Student("Sabina Izdebska", 99)

library1 = Library("Katowice", "Uniwersytecka 5", "21-300",
                   "8:00-20:00", "222-333-444")

library2 = Library("Gliwice", "Zielona 32", "65-332",
                   "10:00-18:00", "123-452-762")

employee1 = Employee("Anna", "Nowak", "1.07.2015",
                     "4.02.1987", "Katowice", "Wiosenna 23",
                     "12-478", "111-777-543")

employee2 = Employee("Karol", "Jakubek", "1.04.2019",
                     "4.02.1971", "Gliwice", "Królewska 219",
                     "09-762", "534-935-034")

employee3 = Employee("Zofia", "Kownacka", "1.11.2004",
                     "4.02.1964", "Chorzów", "Wiejska 123",
                     "84-321", "649-732-323")

book1 = Book(library1, "2.03.2003", "Anna", "Kowal", 231)
book2 = Book(library2, "21.02.1982", "Katarzyna", "Mister", 167)
book3 = Book(library2, "18.09.1955", "Dorota", "Rokita", 285)
book4 = Book(library2, "31.01.2010", "Marian", "Teska", 320)
book5 = Book(library1, "6.12.2020", "Jakub", "Ziemowicz", 98)

order1 = Order(employee3, student1, book4, "22.09.2021")
order2 = Order(employee1, student2, book5, "2.10.2021")

print(order1)
print(order2)
