#!/usr/bin/env python3

def main() -> None:
    string = input("Enter string: ")

    vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    count = 0

    string_len = len(string)

    for i in range(string_len // 2):
        if string[i] in vowels:
            count += 1

    for i in range(string_len // 2, string_len):
        if string[i] in vowels:
            count -= 1

    if count == 0:
        print(True)
    else:
        print(False)

if __name__ == "__main__":
    main()
