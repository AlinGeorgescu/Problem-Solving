#!/usr/bin/env python3

def main() -> None:
    string = input("Insert a string:")
    vowels = {'a', 'e', 'i', 'o', 'u'}

    string = ''.join(filter(lambda c: c not in vowels, string))

    print(string)

if __name__ == "__main__":
    main()
