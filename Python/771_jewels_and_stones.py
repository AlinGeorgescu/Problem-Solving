#!/usr/bin/env python3

def main() -> None:
    J = input("Enter J:")
    S = input("Enter S:")

    print(sum(s in J for s in S))

if __name__ == "__main__":
    main()
