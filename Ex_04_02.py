"""
Завдання 2

Напишіть програму-калькулятор,
яка підтримує такі операції: додавання, віднімання, множення, ділення та піднесення до ступеня.
Програма має видавати повідомлення про помилку та продовжувати роботу під час введення некоректних даних,
діленні на нуль та зведенні нуля в негативний степінь.
"""


def info() -> None:
    print(f'\n1: for sum\n2: for minus\n3: for multiply\n4: for div\n5: for pow\n0: for exit\n')


def sum_(a: int, b: int) -> int:
    return a + b


def arguments() -> tuple:
    print()
    a = int(input('give me first argument: '))
    b = int(input('give me second argument: '))
    return a, b


def minus(a: tuple) -> int:
    return a[0] - a[1]


def multi(a: tuple) -> int:
    return a[0] - a[1]


def pow_(a: tuple) -> float:
    return a[0] ** a[1]


def div_(a: tuple) -> float:
    return a[0] / a[1]


while True:
    info()
    user_choose = input('make your choose: ')
    match user_choose:
        case '1':
            print(f'result = {sum(arguments())}')
        case '2':
            print(f'result = {minus(arguments())}')
        case '3':
            print(f'result = {multi(arguments())}')
        case '4':
            try:
                print(f'result = {div_(arguments())}')
            except Exception as e:
                print(f'Oooops you receive an ERROR: {e}')
        case '5':
            try:
                print(f'result = {pow_(arguments())}')
            except Exception as e:
                print(f'Oooops you receive an ERROR: {e}')
        case '0':
            print('bye bye')
            break
