#!/usr/bin/env python3

"""
This module converts a problem name to a file name following the convention:

ProblemNum_problem_name.py
"""

import re

def main() -> None:
    prob_name = input("Enter leetcode problem name: ").lower()

    file_name = re.sub("\.?(\t| )+", "_", prob_name) + ".py"

    print(file_name)

if __name__ == "__main__":
    main()
