#!/usr/bin/env python3

from typing import Counter

def main() -> None:
    string = input("Enter string: ")

    letters = sorted([c, n] for c, n in Counter(string).items())
    res = []

    while len(res) < len(string):
        for i in range(len(letters)):
            if letters[i][1]:
                res.append(letters[i][0])
                letters[i][1] -= 1

        for i in range(len(letters)):
            if letters[~i][1]:
                res.append(letters[~i][0])
                letters[~i][1] -= 1

    print("".join(res))

if __name__ == "__main__":
    main()
