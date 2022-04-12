#!/usr/bin/env python3

def main() -> None:
    s = input("Enter string: ")

    found_a_letter = False
    length = 0

    for i in range(len(s) - 1, -1, -1):
        if s[i] != ' ':
            found_a_letter = True
            length += 1
        elif found_a_letter:
            print(length)
            return

    print(length)

if __name__ == "__main__":
    main()
