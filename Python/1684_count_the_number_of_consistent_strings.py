#!/usr/bin/env python3

def isAllowed(allowed : dict, word : str) -> bool:
    for c in word:
        if not c in allowed:
            return False

    return True

def main() -> None:
    allowed = input("Enter allowed: ")
    words = list(input("Enter words: ").split(","))

    allowed_dict = {}
    for c in allowed:
        allowed_dict[c] = True

    count = 0
    for word in words:
        if isAllowed(allowed_dict, word):
            count += 1

    print(count)

if __name__ == "__main__":
    main()
