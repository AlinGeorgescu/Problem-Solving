#!/usr/bin/env python3

import ast

def main() -> None:
    arr = ast.literal_eval(input("Enter array: "))
    checked = set()

    for num in arr:
        if num in checked:
            print(num)
        else:
            checked.add(num)

if __name__ == "__main__":
    main()
