#!/usr/bin/env python3

def main() -> None:
    n = int(input("Enter a number: "))

    sum_digits = 0
    prod_digits = 1
    while n:
        digit = n % 10
        sum_digits += digit
        prod_digits *= digit
        n = int(n / 10)

    print(prod_digits - sum_digits)

if __name__ == "__main__":
    main()
