#!/usr/bin/env python3

def main() -> None:
    n = int(input("Enter n: "))

    res = []
    for i in range(1, n // 2 + 1):
        res += [i, -i]

    if n % 2 == 1:
        res.append(0)

    print(res)

if __name__ == "__main__":
    main()
