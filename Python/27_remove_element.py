#!/usr/bin/env python3

import ast

def main() -> None:
    nums = ast.literal_eval(input("Enter nums: "))
    val = int(input("Enter val: "))

    cur_set_pos = 0

    for num in nums:
        if num != val:
            nums[cur_set_pos] = num
            cur_set_pos += 1

    print(cur_set_pos)
    print(nums)

if __name__ == "__main__":
    main()
