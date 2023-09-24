#!/usr/bin/env python3

import string

def main() -> None:
    columnNumber = int(input('Enter columnNumber: '))
    alphabet = string.ascii_uppercase
    size = len(alphabet)
    res = ''

    if columnNumber == 0:
        print('A')
        return

    while columnNumber:
        res += alphabet[(columnNumber - 1) % size]
        columnNumber = (columnNumber - 1) // size

    print(res[::-1])

if __name__ == '__main__':
    main()
