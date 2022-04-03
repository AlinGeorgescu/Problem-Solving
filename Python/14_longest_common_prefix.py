#!/usr/bin/env python3

import ast

def main() -> None:
    strings = ast.literal_eval(input("Enter array: "))
    min_length = 200
    max_len = 0
    longest_string = ""

    if len(strings) == 1:
        print(strings[0])
        return

    for string in strings:
        length = len(string)
        if length < min_length:
            min_length = length

        if length > max_len:
            max_len = length
            longest_string = string

    if min_length == 0:
        print("")
        return

    for i in range(min_length):
        for string in strings:
            if longest_string[i] != string[i]:
                print(longest_string[: i])
                return

    print(longest_string[: min_length])

if __name__ == "__main__":
    main()
