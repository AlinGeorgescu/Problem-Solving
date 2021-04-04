#!/usr/bin/env python3

import ast

def main() -> None:
    grid = ast.literal_eval(input("Enter grid: "))

    m = len(grid[0])
    i = len(grid) - 1
    j = m - 1
    count = 0

    while i >= 0 and j >= 0 and j < m:
        if grid[i][j] < 0:
            count += 1
            j -= 1

            if j < 0:
                i -= 1
                j = m - 1
        else:
            i -= 1
            j = m - 1

    print(count)

if __name__ == "__main__":
    main()
