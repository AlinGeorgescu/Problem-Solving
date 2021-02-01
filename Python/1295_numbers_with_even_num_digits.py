#!/usr/bin/env python3

def main() -> None:
    nums = list(map(int, input("Enter the numbers: ").split(",")))

    print(sum(len(str(n)) % 2 == 0 for n in nums))

if __name__ == "__main__":
    main()
