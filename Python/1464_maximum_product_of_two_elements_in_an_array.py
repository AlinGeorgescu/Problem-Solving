#!/usr/bin/env python3

def main() -> None:
    nums = list(map(int, input("Enter nums: ").split(",")))

    max1 = 0
    max2 = 0

    for i in nums:
        if i > max1:
            max2 = max1
            max1 = i
        elif i > max2:
            max2 = i

    print((max1 - 1) * (max2 - 1))

if __name__ == "__main__":
    main()
