#!/usr/bin/env python3

def isSelfDividing(n : int) -> bool:
    copy = n

    while copy != 0:
        digit = copy % 10

        if (digit == 0) or (n % digit != 0):
            return False

        copy //= 10

    return True

def main() -> None:
    left = int(input("Enter left: "))
    right = int(input("Enter right: "))

    res = []

    for i in range(left, right + 1):
        if (i < 10) or isSelfDividing(i):
            res.append(i)

    print(res)

if __name__ == "__main__":
    main()
