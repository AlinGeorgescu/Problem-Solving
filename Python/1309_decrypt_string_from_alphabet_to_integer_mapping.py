#!/usr/bin/env python3

def main() -> None:
    string = input("Enter string: ")

    res = ""
    i = 0

    while i < len(string) - 2:
        if (string[i + 2] == "#"):
            res += chr(ord('a') + int(string[i : i + 2]) - 1)
            i += 3
        else:
            res += chr(ord('a') + int(string[i]) - 1)
            i += 1

    if string[-1] != "#":
        if string[-2] != "#":
            res += chr(ord('a') + int(string[-2]) - 1)

        res += chr(ord('a') + int(string[-1]) - 1)

    print(res)

if __name__ == "__main__":
    main()
