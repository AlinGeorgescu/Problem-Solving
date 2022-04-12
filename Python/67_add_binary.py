#!/usr/bin/env python3

def main() -> None:
    a = input("Enter a: ")
    b = input("Enter b: ")

    carriage = 0
    i = len(a) - 1
    j = len(b) - 1
    sum_num = ""

    while i >= 0 and j >= 0:
        temp_res = int(a[i]) + int(b[j]) + carriage
        sum_num += str(temp_res % 2)
        carriage = temp_res // 2
        i -= 1
        j -= 1

    while i >= 0:
        temp_res = int(a[i]) + carriage
        sum_num += str(temp_res % 2)
        carriage = temp_res // 2
        i -= 1

    while j >= 0:
        temp_res = int(b[j]) + carriage
        sum_num += str(temp_res % 2)
        carriage = temp_res // 2
        j -= 1

    if carriage:
        print("1" + sum_num[::-1])
    else:
        print(sum_num[::-1])

if __name__ == "__main__":
    main()
