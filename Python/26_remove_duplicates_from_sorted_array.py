#!/usr/bin/env python3

import ast

def main() -> None:
    nums = ast.literal_eval(input("Enter nums: "))

    num_dups = 1

    for i in range(1, len(nums)):
        if nums[i - 1] != nums[i]:
            nums[num_dups] = nums[i]
            num_dups += 1

    print(nums)
    print(num_dups)

if __name__ == "__main__":
    main()
