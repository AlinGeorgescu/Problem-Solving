#!/usr/bin/env python3

import ast

def main() -> None:
    num = input("Enter array: ")

    if num < 0:
        print(False)
        return

    copy = num
    reverse = 0
    while copy:
        reverse = reverse * 10 + copy % 10
        copy //= 10

    print(num == reverse)

if __name__ == "__main__":
    main()
