# -*- coding: utf-8 -*-

from os import urandom
from string import ascii_letters

def generateRandChar():
    '''Generates random ascii character using os.urandom'''

    while True:
        try:
            rand_char = urandom(1)
            rand_char = rand_char.decode('utf-8')
        except UnicodeDecodeError:
            continue

        if rand_char in ascii_letters:
            break

    return rand_char


def generateRandDigit():
    '''Generate random digit using os.urandom'''

    # Генерируем последовательность байтов
    rand_bytes = urandom(1)
    # Преобразуем ее в число, а потом в строку
    rand_string = str(int.from_bytes(rand_bytes, byteorder='big'))

    # Циклом ищем последний символ и берем его
    for i in range(len(rand_string)):
        i = int(i)
        if i == (len(rand_string) - 1):
            rand_char = rand_string[i]

    return rand_char


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

    # Создаем генератор для цикла
    gen = (i for i in range(length))

    # Генерация строки
    for i in gen:
        # Генерируем цифру до тех пор, пока не будет 0 или 1
        while True:
            cycle_choice = int(generateRandDigit())

            if cycle_choice == 0 or cycle_choice == 1:
                break

        # При 0 кидаем в пароль символ латиницы
        if cycle_choice == 0:
            char = generateRandChar()
            pwd += char
        # При 1-е цифру
        else:
            char = generateRandDigit()
            pwd += char

    print(pwd)


if __name__ == '__main__':
    main()
