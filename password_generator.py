from random import choice, randint
from string import ascii_letters


def main():
    pwd = ''

    working = True
    while working:
        try:
            limit = input('Quantity of symbols: \n')
        except KeyboardInterrupt as error:
            print(error)

            return 1

        try:
            limit = int(limit)
        except ValueError:
            print('There is an error.')

            return 1

        if limit <= 0:
            print('You entered a negative number or number less than zero. Try again.')
            continue
        elif limit > 30:
            print('You entered a number more than 30. Try again.')
            continue
        else:
            break

    for i in range(0, limit):
        cycle_choice = randint(0, 1)

        if cycle_choice == 0:
            char = choice(ascii_letters)
            pwd += char
        else:
            char = str(randint(0, 10))
            pwd += char

    print(pwd)


if __name__ == '__main__':
    main()
