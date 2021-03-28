#!/usr/bin/env python3

import ast

def main() -> None:
    mat = ast.literal_eval(input("Enter mat: "))

    j1 = 0
    j2 = len(mat) - 1
    sum = 0

    for row in mat:
        if j1 == j2:
            sum += row[j1]
        else:
            sum += row[j1] + row[j2]

        j1 += 1
        j2 -= 1

    print(sum)

if __name__ == "__main__":
    main()
