#!/usr/bin/env python3

def main() -> None:
    numRows = int(input("Enter numRows: "))
    triangle = [[1]]

    for i in range(1, numRows):
        row = [1]

        for j in range(1, i + 1):
            if j == i:
                row.append(1)
            else:
                row.append(triangle[i - 1][j - 1] +  triangle[i - 1][j])

        triangle.append(row)

    print(triangle)

if __name__ == "__main__":
    main()
