#!/usr/bin/env python3

def main() -> None:
    s = input("Enter string: ")
    indices = list(map(int, input("Enter indices: ").split(",")))

    res = [''] * len(s)
    for index, char in enumerate(s):
        res[indices[index]] = char

    print("".join(res))

if __name__ == "__main__":
    main()
