#!/usr/bin/env python3

import ast

def main() -> None:
    points = ast.literal_eval(input("Enter points: "))

    time = sum(max(abs(points[i][0] - points[i - 1][0]), \
                   abs(points[i][1] - points[i - 1][1])) \
                       for i in range(1, len(points)))

    print(time)

if __name__ == "__main__":
    main()
