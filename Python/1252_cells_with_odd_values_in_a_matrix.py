#!/usr/bin/env python3

import ast

def main() -> None:
    m = int(input("Enter m: "))
    n = int(input("Enter n: "))
    indices = ast.literal_eval(input("Enter indices: "))

    odd_rows = [False] * m
    odd_cols = [False] * n
    for row, col in indices:
        odd_rows[row] ^= True
        odd_cols[col] ^= True

    print(sum(row ^ col for row in odd_rows for col in odd_cols))


if __name__ == "__main__":
    main()
