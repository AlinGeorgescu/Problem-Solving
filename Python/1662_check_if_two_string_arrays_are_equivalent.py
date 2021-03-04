#!/usr/bin/env python3

def main() -> None:
    word1 = list(input("Enter word1: ").split(","))
    word2 = list(input("Enter word2: ").split(","))

    i = 0
    j = 0
    s1 = 0
    s2 = 0
    while i < len(word1) and j < len(word2):
        while s1 < len(word1[i]) and s2 < len(word2[j]):
            if word1[i][s1] != word2[j][s2]:
                print("false")
                return
            else:
                s1 += 1
                s2 += 1

        if s1 == len(word1[i]):
            i += 1
            s1 = 0
        if s2 == len(word2[j]):
            j += 1
            s2 = 0

    if i == len(word1) and j == len(word2):
        print("true")
    else:
        print("false")

if __name__ == "__main__":
    main()
