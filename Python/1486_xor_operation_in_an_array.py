#!/usr/bin/env python3

def main() -> None:
    n = input("Enter n: ")
    start = input("Enter first: ")

    last = start + 2 * (n - 1)

    if start % 4 <= 1:
        if n % 4 == 1:
            res = last
        elif n % 4 == 2:
            res = 2
        elif n % 4 == 3:
            res = 2 ^ last
        else:
            res = 0

    else:
        if n % 4 == 1:
            res = start
        elif n % 4 == 2:
            res = start ^ last
        elif n % 4 == 3:
            res = start ^ 2
        else:
            res = start ^ 2 ^ last

    print(res)

if __name__ == "__main__":
    main()
