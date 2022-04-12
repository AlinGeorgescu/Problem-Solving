#!/usr/bin/env python3

def main() -> None:
    x = int(input("Enter x: "))

    if x == 1:
            return 1

    root = x // 2

    while root**2 > x:
        root = (root + x // root) // 2

    print(root)

if __name__ == "__main__":
    main()
