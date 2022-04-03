#!/usr/bin/env python3

import ast

def main() -> None:
    nums = ast.literal_eval(input("Enter nums: "))
    target = int(input("Enter target: "))

    if target < nums[0]:
        print(0)
        return

    len_nums = len(nums)
    if target > nums[-1]:
        print(len_nums)
        return

    start = 0
    end = len_nums - 1
    mid = (start + end) // 2

    while nums[mid] != target:
        if start == end or start == end - 1:
            print(start + 1)
            return

        if nums[mid] > target:
            end = mid
        else:
            start = mid

        mid = (start + end) // 2

    print(mid)


if __name__ == "__main__":
    main()
