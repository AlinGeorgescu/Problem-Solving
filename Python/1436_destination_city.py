#!/usr/bin/env python3

import ast

def main() -> None:
    paths = ast.literal_eval(input("Enter paths: "))

    out_path = set()
    in_path = set()

    for city_a, city_b in paths:
        out_path.add(city_a)
        in_path.add(city_b)

    for city in in_path:
        if city not in out_path:
            print(city)
            return

if __name__ == "__main__":
    main()
