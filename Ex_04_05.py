"""Завдання 5

Створіть програму спортивного комплексу, у якій передбачене меню:
1 - перелік видів спорту,
2 - команда тренерів,
3 - розклад тренувань,
4 - вартість тренування.

Дані зберігати у словниках. Також передбачити пошук по прізвищу тренера,
яке вводиться з клавіатури у відповідному пункті меню.
Якщо ключ не буде знайдений, створити відповідний клас-Exception, який буде викликатися в обробнику виключень.
"""

GYM = {'sports': ['football', 'basketball', 'hockey'],
       'trainers': ['Moghuchih', 'Pelyckh', 'Kononenko'],
       'schedules': ['monday-friday', 'once a week'],
       'coasts': [1500, 100]
       }


class TrainerNotFound(Exception):

    def __str__(self):
        return 'We don`t have such coach in our GYM'


def info() -> None:
    print('\nMenu:')
    print('1 - види спорту\n2 - команда тренерів,\n3 - розклад тренувань,\n4 - вартість тренування\n5 - пошук за тренером\n0 - вихід')


def coach_check(user_input: str) -> bool:
    for coach in GYM['trainers']:
        if user_input.lower() == coach.lower():
            return True
    return False


while True:
    info()
    user_choose = input('\nmake your choose: ')
    match user_choose:
        case '1':
            print(f'In our GYM we have such sports: {GYM["sports"]}')
        case '2':
            print(f'Our coaches: {GYM["trainers"]}')
        case '3':
            print(f'We have such schedules: {GYM["schedules"]}')
        case '4':
            print(f'Our prices: {GYM["coasts"]}')
        case '5':
            coach_search = input('Who are you looking for: ')
            try:
                if coach_check(coach_search):
                    print(f'We do have a coach {coach_search}')
                else:
                    raise TrainerNotFound
            except Exception as e:
                print(e)
        case '0':
            print('bye, bye')
            break
