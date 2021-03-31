#!/usr/bin/env python3

def main() -> None:
    n = int(input("Enter n: "))

    if n % 2 == 0:
        return "a" * (n - 1) + "b"

    return "a" * n

if __name__ == "__main__":
    main()
