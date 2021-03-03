#!/usr/bin/env python3

import ast

def main() -> None:
    items = ast.literal_eval(input("Enter items: "))
    ruleKey = input("Enter ruleKey: ")
    ruleValue = input("Enter ruleVal: ")

    if ruleKey == "type":
        ruleKey = 0
    elif ruleKey == "color":
        ruleKey = 1
    else:
        ruleKey = 2

    print(sum(1 if x[ruleKey] == ruleValue else 0 for x in items))

if __name__ == "__main__":
    main()
