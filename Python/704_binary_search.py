#!/usr/bin/env python3

import ast

def main() -> None:
    nums = ast.literal_eval(input("Enter nums: "))
    target = int(input("Enter target: "))

    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = (start + end) // 2

        if target == nums[mid]:
            print(mid)
            return
        elif target > nums[mid]:
            start = mid + 1
        else:
            end = mid - 1

    print(-1)

if __name__ == "__main__":
    main()