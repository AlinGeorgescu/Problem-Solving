#!/usr/bin/env python3

def main() -> None:
    word1 = input("Enter word1: ")
    word2 = input("Enter word2: ")

    i = j = 0
    res = ""

    while i < len(word1) and j < len(word2):
        res += word1[i] + word2[j]
        i += 1
        j += 1

    while i < len(word1):
        res += word1[i]
        i += 1

    while j < len(word2):
        res += word2[j]
        j += 1

    print(res)

if __name__ == "__main__":
    main()
