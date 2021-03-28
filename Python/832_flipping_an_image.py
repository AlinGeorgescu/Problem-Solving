#!/usr/bin/env python3

import ast

def main() -> None:
    image = ast.literal_eval(input("Enter indices: "))

    img_size = len(image)
    for row in image:
        for i in range(img_size // 2):
            tmp = row[img_size - i - 1]
            row[img_size - i - 1] = row[i] ^ 1
            row[i] = tmp ^ 1
        if img_size % 2 != 0:
            row[img_size // 2] ^= 1

    print(image)

if __name__ == "__main__":
    main()
