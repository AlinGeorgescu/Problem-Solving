#!/usr/bin/env python3

import ast

def main() -> None:
    arr = ast.literal_eval(input("Enter array: "))

    l = len(arr)

    if l % 2 == 1:
        y = arr[l // 2]
    else:
        y = (arr[l // 2] + arr[(l - 2) // 2]) // 2

    cost = 0
    for i in range(l):
        cost += abs(arr[i] - y)

    print(cost)

if __name__ == "__main__":
    main()
