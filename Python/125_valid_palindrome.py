#!/usr/bin/env python3

def main() -> None:
    s = input("Enter s: ")

    i = 0
    j = len(s) - 1

    while i < j:
        while not s[i].isalnum() and i < j:
            i += 1

        while not s[j].isalnum() and i < j:
            j -= 1

        if s[i].lower() != s[j].lower():
            print('False')

        i += 1
        j -= 1

    print('True')

if __name__ == "__main__":
    main()
