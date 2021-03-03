#!/usr/bin/env python3

import ast

def main() -> None:
    accounts = ast.literal_eval(input("Enter client: "))

    maxi = 0

    for clnt in accounts:
        cur = sum(map(int, clnt))
        if cur > maxi:
            maxi = cur

    print(maxi)

if __name__ == "__main__":
    main()
