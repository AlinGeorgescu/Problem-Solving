#!/usr/bin/env python3

import ast

def main() -> None:
    digits = ast.literal_eval(input("Enter num: "))

    temp_res = 0

    for i in range(len(digits) - 1, -1, -1):
        temp_res = digits[i] + 1

        if temp_res == 10:
            digits[i] = 0
        else:
            digits[i] = temp_res
            print(digits)
            return

    if temp_res == 10:
        print([1] + digits)

if __name__ == "__main__":
    main()
