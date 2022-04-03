#!/usr/bin/env python3

def main() -> None:
    string = input("Enter string: ")

    opened_parantheses_map = {
        '(': ')',
        '{': '}',
        '[': ']'
    }

    closed_parantheses_map = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    stack = []

    for paranthesis in string:
        if paranthesis in closed_parantheses_map:
            if len(stack) > 0 and stack[-1] == closed_parantheses_map[paranthesis]:
                stack.pop()
            else:
                print(False)
                return
        else:
            stack.append(paranthesis)

    if len(stack) == 0:
        print(True)
    else:
        print(False)

if __name__ == "__main__":
    main()
