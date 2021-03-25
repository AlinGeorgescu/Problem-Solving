#!/usr/bin/env python3

def main() -> None:
    str = input("Enter str: ")

    # print(str.lower())

    print("".join(chr(ord(c) + 32) if "A" <= c <= "Z" else c for c in str))


if __name__ == "__main__":
    main()