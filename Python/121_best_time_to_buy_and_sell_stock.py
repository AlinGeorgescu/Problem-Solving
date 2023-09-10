#!/usr/bin/env python3

import ast
import sys

def main() -> None:
    prices = ast.literal_eval(input("Enter prices: "))

    cur_min = sys.maxsize
    max_profit = 0

    for price in prices:
        cur_min = min(price, cur_min)
        max_profit = max(price - cur_min, max_profit)

    print(max_profit)

if __name__ == "__main__":
    main()
