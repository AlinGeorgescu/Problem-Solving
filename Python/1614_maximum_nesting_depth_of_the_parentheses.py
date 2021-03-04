#!/usr/bin/env python3

def main() -> None:
    s = input("Enter s: ")
    depth = 0
    max_depth = 0

    for c in s:
        if c == "(":
            depth += 1

            if depth > max_depth:
                max_depth = depth

        elif c == ")":
            depth -= 1

    print(max_depth)

if __name__ == "__main__":
    main()
