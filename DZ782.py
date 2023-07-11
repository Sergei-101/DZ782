
from random import randint
import sys

# Задание №1
# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.


__all__ = ['date_validate']

_LEAP = 4
_END_DAY = 31
_START_DAY = 1
_END_MONTH = 12
_START_MONTH = 1
_END_YEAR = 9999
_START_YEAR = 1


def date_validate(date: str) -> bool:
    day, month, year = map(int, date.split('.'))
    return ((_END_DAY >= day >= _START_DAY) and
            (_END_MONTH >= month >= _START_MONTH) and
            (_END_YEAR >= year >= _START_YEAR))


def _is_leap_year(date: str) -> bool:
    day, month, year = map(int, date.split('.'))
    if year % _LEAP == 0:
        return True
    return False

if __name__ == "__main__":
    date = sys.argv[1]
    print(date_validate(date))


# Задание 2
# Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код,
# решающий задачу о 8 ферзях. Известно, что на доске 8×8 можно расставить 8 ферзей так,
# чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске, определите,
# есть ли среди них пара бьющих друг друга. Программа получает на вход восемь пар чисел,
# каждое число от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните истину,
# а если бьют - ложь. Напишите функцию в шахматный модуль. Используйте генератор случайных чисел
# для случайной расстановки ферзей в задаче выше. Проверяйте различный случайные варианты и
# выведите 4 успешных расстановки. (когда ферзи не бьют друг друга)

def ferz():
    """
    Задача о 8 ферзях

    """
    print("Введите действие:\n"
          "1 - Сгенерировать координаты ферзей\n"
          "2 - Ввести кординаты ферзей\n"
          "3 - Вывести расположение ферзей на доске\n"
          "4 - Вывести бьюь друг друга ферзи или нет\n"
          "5 - Вывести успешную расстановку ферзей\n"
          "6 - Выйти")
    x = []
    y = []
    count_ferz = 8
    while True:
        com_str = int(input("Введите цифру - "))
        if com_str == 1:
            x = []
            y = []
            for i in range(count_ferz):
                new_x, new_y = randint(0, count_ferz - 1), randint(0, count_ferz - 1)
                x.append(int(new_x))
                y.append(int(new_y))
        elif com_str == 2:
            x = []
            y = []
            for i in range(count_ferz):
                new_x, new_y = input("Введите значение через пробел - ").split()
                x.append(int(new_x))
                y.append(int(new_y))
        elif com_str == 3:
            matrix = [[0 for i in range(8)] for j in range(8)]
            for i in range(count_ferz):
                matrix[x[i]][y[i]] = 1
            print(*matrix, sep="\n")
        elif com_str == 4:
            correct = True

            for i in range(count_ferz):
                for j in range(i + 1, count_ferz):
                    if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                        correct = False
            if correct:
                print('False')
            else:
                print('True')
        elif com_str == 5:
            correct = True
            while correct:
                x = []
                y = []
                for i in range(count_ferz):
                    new_x, new_y = randint(0, count_ferz - 1), randint(0, count_ferz - 1)
                    x.append(int(new_x))
                    y.append(int(new_y))

                for i in range(count_ferz):
                    for j in range(i + 1, count_ferz):
                        if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):

                            correct = False
            print(x, y)
        elif com_str == 6:
            break
        else:
            break
ferz()
