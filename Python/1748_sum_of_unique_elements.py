#!/usr/bin/env python3

import ast

def main() -> None:
    nums = ast.literal_eval(input("Enter nums: "))

    freqs = {}

    for num in nums:
        if num in freqs:
            freqs[num] += 1
        else:
            freqs[num] = 1

    sum = 0

    for num, freq  in freqs.items():
        if freq == 1:
            sum += num

    print(sum)

if __name__ == "__main__":
    main()
