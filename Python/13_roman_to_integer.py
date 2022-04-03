#!/usr/bin/env python3

def main() -> None:
    number_mapping = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    s = input("Enter number: ").strip()

    converted_number = list(map(lambda letter: number_mapping[letter], s))

    prev_letter = converted_number[0]
    final_number = 0
    length = len(s)
    i = 1

    while i < length:
        curr_letter = converted_number[i]

        if prev_letter < curr_letter:
            final_number += curr_letter - prev_letter

            if i + 1 < length:
                prev_letter = converted_number[i + 1]
            else:
                prev_letter = 0

            i += 2
        else:
            final_number += prev_letter
            prev_letter = curr_letter
            i += 1

    final_number += prev_letter
    print(final_number)


if __name__ == "__main__":
    main()
