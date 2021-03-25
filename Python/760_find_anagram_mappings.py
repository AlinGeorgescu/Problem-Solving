#!/usr/bin/env python3

from collections import defaultdict

def main() -> None:
    a = list(map(int, input("Enter A: ").split(",")))
    b = list(map(int, input("Enter B: ").split(",")))

    indexes = defaultdict(lambda: [])
    for i, item in enumerate(b):
        indexes[item].append(i)

    res = []
    for item in a:
        res.append(indexes[item].pop())

    print(res)

if __name__ == "__main__":
    main()
