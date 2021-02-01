#!/usr/bin/env python3

import collections

def main() -> None:
    nums = list(map(int, input("Enter the numbers: ").split(",")))

    count = collections.Counter(nums)

    for i in range(1,101):
        count[i] += count[i-1]

    res = [count[x-1] for x in nums]

    print(res)

if __name__ == "__main__":
    main()
