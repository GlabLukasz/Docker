#!/usr/bin/python3

from random import randit

min_number=init(input('Please insert minimal number: '))
max_number=init(input('Please insert maximal number: '))

def main():
    if max_number < min_number:
        print('Invalid input')
    else:
        rnd_number=randit(min_number, max_number)
        print(rnd_number)

if __name__ == "__main__":
    main()