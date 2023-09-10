#!/usr/bin/env python3

def main() -> None:
    rowIndex = int(input("Enter rowIndex: "))
    last_row = [1]

    for i in range(1, rowIndex + 1):
        row = [1]

        for j in range(1, i + 1):
            if j == i:
                row.append(1)
            else:
                row.append(last_row[j - 1] +  last_row[j])

        last_row = row

    print(last_row)

if __name__ == "__main__":
    main()
