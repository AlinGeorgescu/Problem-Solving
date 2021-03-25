#!/usr/bin/env python3

def main() -> None:
    arr = list(map(int, input("Enter arr: ").split(",")))
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = int(input("Enter c: "))

    num = 0

    for k in range(len(arr)):
        for j in range(k):
            for i in range(j):
                if abs(arr[i] - arr[j]) <= a and      \
                        abs(arr[j] - arr[k]) <= b and \
                        abs(arr[i] - arr[k]) <= c:
                    num += 1

    print(num)

if __name__ == "__main__":
    main()
