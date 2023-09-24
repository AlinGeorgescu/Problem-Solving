#!/usr/bin/env python3

import ast

def main() -> None:
    nums = ast.literal_eval(input('Enter nums: '))
    items = {}

    for num in nums:
        if num in items:
            items[num] += 1
        else:
            items[num] = 1

    maximum = 0
    item = 0

    for key, val in items.items():
        if val > maximum:
            maximum = val
            item = key

    print(item)

def optimal_solution() -> None:
    nums = ast.literal_eval(input('Enter nums: '))
    item = nums[0]
    count = 0

    for num in nums:
        if count == 0:
            item = num
            count = 1
        elif item == num:
            count += 1
        else:
            count -= 1

if __name__ == '__main__':
    main()
