#!/usr/bin/env python3

import ast

def main() -> None:
    prices = ast.literal_eval(input("Enter prices: "))

    stack = []
    for i, price in enumerate(prices):
        while len(stack) > 0 and prices[stack[-1]] >= price:
            prices[stack.pop()] -= price

        stack.append(i)

    print(prices)

if __name__ == "__main__":
    main()
