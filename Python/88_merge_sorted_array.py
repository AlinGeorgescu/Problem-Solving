#!/usr/bin/env python3

import ast

def main() -> None:
    nums1 = ast.literal_eval(input("Enter nums1: "))
    m = int(input("Enter m: "))
    nums2 = ast.literal_eval(input("Enter nums2: "))
    n = int(input("Enter n: "))

    k = m + n - 1
    m -= 1
    n -= 1

    while m >= 0 and n >= 0:
        if nums1[m] > nums2[n]:
            nums1[k] = nums1[m]
            m -= 1
            k -= 1
        else:
            nums1[k] = nums2[n]
            n -= 1
            k -= 1

    while n >= 0:
        nums1[k] = nums2[n]
        n -= 1
        k -= 1

    print(nums1)

if __name__ == "__main__":
    main()
