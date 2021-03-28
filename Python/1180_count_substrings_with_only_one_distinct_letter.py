#!/usr/bin/env python3

def main() -> None:
    string = input("Enter string: ")

    prev = ""
    num = 0
    len_seq = 0

    for c in string:
        if c == prev:
            len_seq += 1
        else:
            num += len_seq * (len_seq + 1) // 2
            len_seq = 1

        prev = c

    num += len_seq * (len_seq + 1) // 2

    print(num)

if __name__ == "__main__":
    main()
