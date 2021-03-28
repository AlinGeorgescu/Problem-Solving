#!/usr/bin/env python3

def main() -> None:
    string = input("Enter string: ")

    res = ""
    paren_count = 0

    for c in string:
        if c == "(" and paren_count == 0:
            paren_count += 1
        elif c == "(":
            paren_count += 1
            res += "("
        elif c == ")" and paren_count == 1:
            paren_count -= 1
        else:
            paren_count -= 1
            res += ")"

    print(res)

if __name__ == "__main__":
    main()
