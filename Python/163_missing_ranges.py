#!/usr/bin/env python3

import ast

def main() -> None:
    nums = ast.literal_eval(input('Enter nums: '))
    lower = int(input('Enter lower: '))
    upper = int(input('Enter upper: '))

    result = []
    last = lower
    nums.append(upper + 1)

    for num in nums:
        if num == last + 2:
            result.append(str(last + 1))
        elif num > last + 2:
            result.append(str(last + 1) + '->' + str(num - 1))

        last = num

    print(result)

if __name__ == '__main__':
    main()
