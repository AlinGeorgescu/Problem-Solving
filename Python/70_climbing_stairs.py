#!/usr/bin/env python3

def main() -> None:
    n = int(input("Enter n: "))

    f1 = 1
    f2 = 2

    while n > 1:
        f3 = f2 + f1
        f1 = f2
        f2 = f3
        n -= 1

    print(f1)

if __name__ == "__main__":
    main()
