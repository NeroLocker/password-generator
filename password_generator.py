# -*- coding: utf-8 -*-

from random import choice, randint
from string import ascii_letters


def gen(limit):
    '''Generator for cycle'''
    for i in range(0, limit):
        yield i


def main():
    # Output password
    pwd = ''

    while True:
        # Исключаем прерывания ввода
        try:
            length = input('Quantity of symbols: \n')
        except KeyboardInterrupt as error:
            print(error)

            return 1

        # Ловим ошибку преобразования типов
        try:
            length = int(length)
        except ValueError:
            print('There is an error. Try again')

            continue

        # Проверка длины пароля
        if length <= 0:
            print('You entered a negative number or number less than zero. Try again.')
            continue
        elif length > 35:
            print('You entered a number more than 35. Try again.')
            continue
        else:
            break

    # Генерация строки
    for i in gen(length):
        cycle_choice = randint(0, 1)

        if cycle_choice == 0:
            char = choice(ascii_letters)
            pwd += char
        else:
            char = str(randint(0, 9))
            pwd += char

    print(pwd)


if __name__ == '__main__':
    main()
