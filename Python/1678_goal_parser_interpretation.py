#!/usr/bin/env python3

def main() -> None:
    command = input("Enter command: ")
    command = command.replace("(al)", "al").replace("()", "o")
    print(command)

if __name__ == "__main__":
    main()
