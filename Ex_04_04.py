"""
Завдання 4

Опишіть свій клас винятку. Напишіть функцію, яка викидатиме цей виняток,
якщо користувач введе певне значення, і перехопіть цей виняток під час виклику функції.

"""


class MyException(Exception):
    pass


def main():
    try:
        text_input = input('input some text: ')
        if 'rus' in text_input:
            raise MyException
        else:
            print('our text is Ok')
    except MyException:
        print('ruzzians not allowed')


if __name__ == '__main__':
    main()
