#!/usr/bin/env python3

def main() -> None:
    nums = list(map(int, input("Enter nums: ").split(",")))

    freq = {}
    for i in nums:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    num_pairs = 0
    for val in freq.values():
        num_pairs += (val * (val - 1)) // 2

    print(num_pairs)

if __name__ == "__main__":
    main()
