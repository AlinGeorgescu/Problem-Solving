#!/usr/bin/env python3

def main() -> None:
    nums = input("Insert list: ")
    nums = list(map(int, nums.split(', ')))
    nums = [x for a, b in zip(nums[0::2], nums[1::2]) for x in [b] * a]
    print(nums)

if __name__ == "__main__":
    main()
