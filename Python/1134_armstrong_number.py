#!/usr/bin/env python3

def main() -> None:
    number = int(input("Enter number: "))

    copy = number
    digits = []
    num_digits = 0

    while copy != 0:
        digits.append(copy % 10)
        copy //= 10
        num_digits += 1

    res = sum([digit ** num_digits for digit in digits])
    if res == number:
        print(True)
    else:
        print(False)

if __name__ == "__main__":
    main()
