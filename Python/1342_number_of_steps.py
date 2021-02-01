#!/usr/bin/env python3

from math import floor, log

def main() -> None:
    steps = 0
    x = int(input("Enter a number: "))

    while (x):
        if (x % 2 == 0):
            x /= 2
        else:
            x -= 1
        steps += 1

    print("Number of steps: %d" % steps)

if __name__ == "__main__":
    main()
