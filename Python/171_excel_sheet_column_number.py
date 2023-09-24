#!/usr/bin/env python3

import string

def main() -> None:
    columnTitle = input('Enter columnTitle: ')
    alphabet = dict((letter, index) for index, letter in enumerate(string.ascii_uppercase))
    pow = len(string.ascii_uppercase)
    len_title = len(columnTitle)
    index = 0

    for i in range(len_title - 1, -1, -1):
        index += (alphabet[columnTitle[i]] + 1) * pow ** (len_title - i - 1)

    print(index)

if __name__ == '__main__':
    main()
