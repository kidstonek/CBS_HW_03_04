"""
Завдання 3

Опишіть клас співробітника, який вміщує такі поля: ім'я, прізвище, відділ і рік початку роботи.
Конструктор має генерувати виняток, якщо вказано неправильні дані.
Введіть список працівників із клавіатури.
Виведіть усіх співробітників, які були прийняті після цього року.

"""


class Employee:
    def __init__(self, name: str, surname: str, department: str, start_work_year: int):
        self.name = name
        self.surname = surname
        self.department = department
        self.start_work_year = start_work_year


person1 = Employee('And', )