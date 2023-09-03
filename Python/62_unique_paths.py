#!/usr/bin/env python3

import math

def main() -> None:
    m = int(input("Enter m: "))
    n = int(input("Enter n: "))

    print(math.factorial(m + n - 2) / math.factorial(m - 1) / math.factorial(n - 1))

if __name__ == "__main__":
    main()