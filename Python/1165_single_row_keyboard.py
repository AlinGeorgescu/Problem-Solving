#!/usr/bin/env python3

def main() -> None:
    keyboard = input("Enter keyboard: ")
    word = input("Enter word: ")

    pos_key = {}
    for (i, c) in enumerate(keyboard):
        pos_key[c] = i

    count = 0
    last_pos = 0
    for c in word:
        count += abs(pos_key[c] - last_pos)
        last_pos = pos_key[c]

    print(count)

if __name__ == "__main__":
    main()
