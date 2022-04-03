#!/usr/bin/env python3

import ast

def main() -> None:
    list1 = ast.literal_eval(input("Enter list1: "))
    list2 = ast.literal_eval(input("Enter list2: "))

    len1 = len(list1)
    len2 = len(list2)
    i = j = 0
    res = []

    while i < len1 and j < len2:
        if list1[i] < list2[j]:
            res.append(list1[i])
            i += 1
        else:
            res.append(list2[j])
            j += 1

    if i < len1:
        res += list1[i :]

    if j < len2:
        res += list2[j :]

    print(res)

if __name__ == "__main__":
    main()
