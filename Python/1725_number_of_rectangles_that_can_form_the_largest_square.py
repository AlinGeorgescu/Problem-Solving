#!/usr/bin/env python3

import ast

def main() -> None:
    rectangles = ast.literal_eval(input("Enter rectangles: "))

    squares = [min(rectangle) for rectangle in rectangles]

    max = 0
    num_rectangles = 0
    for square in squares:
        if square > max:
            max = square
            num_rectangles = 1
        elif square == max:
            num_rectangles += 1

    print(num_rectangles)

if __name__ == "__main__":
    main()
