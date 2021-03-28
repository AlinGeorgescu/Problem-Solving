#!/usr/bin/env python3

def main() -> None:
    number = int(input("Enter number: "))

    num_digits_after = 0
    num_digits = 0
    copy = number

    while copy != 0:
        if copy % 10 == 6:
            num_digits_after = num_digits

        num_digits += 1
        copy //= 10

    if num_digits_after == 0:
        if number % 10 == 6:
            res = number + 3
        else:
            res = number
    else:
        res = number + 3 * (10 ** num_digits_after)

    print(res)

if __name__ == "__main__":
    main()
