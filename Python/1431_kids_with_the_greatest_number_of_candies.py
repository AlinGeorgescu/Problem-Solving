#!/usr/bin/env python3

def main() -> None:
    candies = list(map(int, input("Enter candies: ").split(",")))
    extraCandies = int(input("Enter extraCandies: "))
    max_num = max(candies)
    print(list(map(lambda x: x + extraCandies >= max_num, candies)))

if __name__ == "__main__":
    main()
