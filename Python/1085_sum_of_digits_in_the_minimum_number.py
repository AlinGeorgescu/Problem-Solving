#!/usr/bin/env python3

import ast

def digitSum(n : int) -> int:
    sum = 0

    while n != 0:
        sum += n % 10
        n //= 10

    return sum

def main() -> None:
    nums = ast.literal_eval(input("Enter nums: "))

    minimum = min(nums)

    if minimum < 10:
        print((minimum % 2) ^ 1)
    else:
        print((digitSum(minimum) % 2) ^ 1)

if __name__ == "__main__":
    main()
