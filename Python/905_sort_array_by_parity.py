#!/usr/bin/env python3

import ast

def main() -> None:
    arr = ast.literal_eval(input("Enter array: "))

    beg = 0
    end = len(arr) - 1

    while end > 0 and arr[end] % 2 == 1:
        end -= 1

    while beg <= end:
        if arr[beg] % 2 == 0:
            beg += 1
        else:
            arr[beg], arr[end] = arr[end], arr[beg]
            end -= 1

    print(arr)

if __name__ == "__main__":
    main()
