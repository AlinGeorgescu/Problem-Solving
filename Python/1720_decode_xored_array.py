#!/usr/bin/env python3

def main() -> None:
    encoded = list(map(int, input("Enter encoded: ").split(",")))
    first = int(input("Enter first: "))

    res = [first]
    for i in encoded:
        first = i ^ first
        res.append(first)

    print(res)

if __name__ == "__main__":
    main()
