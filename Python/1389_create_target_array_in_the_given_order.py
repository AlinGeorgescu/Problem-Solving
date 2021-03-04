#!/usr/bin/env python3

def main() -> None:
    nums = list(map(int, input("Enter nums: ").split(",")))
    index  = list(map(int, input("Enter index: ").split(",")))

    res = []
    for i in range(len(nums)):
        if index[i] == len(res) :
            res.append(nums[i])
        else:
            res[index[i]:index[i]] = [nums[i]]
    print(res)

if __name__ == "__main__":
    main()
