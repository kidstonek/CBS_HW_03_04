"""
Завдання 3

Опишіть клас співробітника, який вміщує такі поля: ім'я, прізвище, відділ і рік початку роботи.
Конструктор має генерувати виняток, якщо вказано неправильні дані.
Введіть список працівників із клавіатури.
Виведіть усіх співробітників, які були прийняті після цього року.

"""


class EmployeeYearError(Exception):
    pass


class Employee:
    list_of_employees = []

    def __init__(self, name: str, surname: str, department: str, start_work_year: int):
        self.name = name
        self.surname = surname
        self.department = department
        if isinstance(start_work_year, int):
            self.start_work_year = start_work_year
        else:
            raise EmployeeYearError(f'Employee {self.name} from {self.department} department have a problem with year '
                                    f'it is not int')
        self.list_of_employees.append([self.name, self.surname, self.department, self.start_work_year])


if __name__ == '__main__':
    my_test_employees = [['John', 'Cirby', 'IT', '2021'], ['Valera', 'Robinson', 'Log', 1021], ['Dima', 'Johnson', 'Fin', 1991]]
    employees_ = ['person1', 'person2', 'person3']

    for employee, name_of_employee in zip(my_test_employees, employees_):
        try:
            name_of_employee = Employee(*employee)
        except EmployeeYearError as e:
            print(e)

    year_to_search = int(input('\nwhat year we a looking for: '))

    for employee in Employee.list_of_employees:
        if employee[3] > year_to_search:
            print(employee)
