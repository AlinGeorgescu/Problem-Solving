#!/usr/bin/env python3

def main() -> None:
    string = input("Enter the string: ")
    count = 0
    balanced = 0

    for c in string:
        if c == 'L':
            balanced -= 1
        else:
            balanced += 1

        if balanced == 0:
            count += 1

    print(count)

if __name__ == "__main__":
    main()
