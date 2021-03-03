#!/usr/bin/env python3

def main() -> None:
    nums = list(map(int, input("Enter nums: ").split(",")))
    half = len(nums) // 2
    res = []

    i = 0
    j = half
    for k in range(half):
        print(i)
        print(j)
        res.append(nums[i])
        res.append(nums[j])
        i += 1
        j += 1

    print(res)

if __name__ == "__main__":
    main()
