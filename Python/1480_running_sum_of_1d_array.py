#!/usr/bin/env python3

from typing import List

def main(nums: List[int]) -> List[int]:
        runningSum = []
        sum = 0

        for x in nums:
                sum += x
                runningSum.append(sum)

        return runningSum

if __name__ == "__main__":
    n = int(input("Enter number of elements: "))
    a = list(map(int, input("\nEnter the numbers: ").strip().split()))[:n]

    print(main(a))
