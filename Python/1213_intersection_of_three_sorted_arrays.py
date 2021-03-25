#!/usr/bin/env python3

def main() -> None:
    arr1 = list(map(int, input("Enter arr1: ").split(",")))
    arr2 = list(map(int, input("Enter arr2 ").split(",")))
    arr3 = list(map(int, input("Enter arr3: ").split(",")))

    intersection = []

    i = 0
    j = 0
    k = 0

    while True:
        if i >= len(arr1) or j >= len(arr2) or k >= len(arr3):
            break

        if arr1[i] == arr2[j] and arr2[j] == arr3[k]:
            intersection.append(arr1[i])
            i += 1
            j += 1
            k += 1
        else:
            if arr1[i] < arr2[j] or arr1[i] < arr3[k]:
                i += 1
                if i >= len(arr1):
                    break
            if arr2[j] < arr1[i] or arr2[j] < arr3[k]:
                j += 1
                if j >= len(arr2):
                    break
            if arr3[k] < arr1[i] or arr3[k] < arr2[j]:
                k += 1
                if k >= len(arr3):
                    break

    print(intersection)

if __name__ == "__main__":
    main()
