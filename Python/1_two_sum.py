#!/usr/bin/env python3

import ast

def main() -> None:
    nums = ast.literal_eval(input("Enter array: "))
    target = ast.literal_eval(input("Enter target: "))

    checked = {}

    for i, num in enumerate(nums):
        diff = target - num

        if diff in checked:
            print([checked[diff], i])
        else:
            checked[num] = i

if __name__ == "__main__":
    main()
