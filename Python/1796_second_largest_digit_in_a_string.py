#!/usr/bin/env python3

def main() -> None:
    string = input("Enter string: ")
    max1 = -1
    max2 = -1

    for c in string:
        if c.isdigit():
            chr = int(c)
            if chr > max1:
                max2 = max1
                max1 = chr
            elif chr != max1 and chr > max2:
                max2 = chr

    print(max2)

if __name__ == "__main__":
    main()
