#!/usr/bin/env python3

def main() -> None:
    arr = list(map(int, input("Enter arr: ").split(",")))

    len_arr = len(arr)
    sum = 0

    for i in range(len_arr):
        sum += (((i + 1) * (len_arr - i) + 1) // 2) * arr[i]

    print(sum)

if __name__ == "__main__":
    main()
