#!/usr/bin/env python3

import ast

def main() -> None:
    nums = ast.literal_eval(input("Enter nums: "))

    res = nums[0]
    seq = 0

    for i in nums:
        seq = max(seq + i, i)
        res = max(res, seq)

    print(res)

if __name__ == "__main__":
    main()
