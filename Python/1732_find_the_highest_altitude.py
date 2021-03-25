#!/usr/bin/env python3

def main() -> None:
    gain = list(map(int, input("Enter gain: ").split(",")))

    max = 0
    cur_alt = 0
    for alt_dif in gain:
        cur_alt += alt_dif

        if cur_alt > max:
            max = cur_alt

    print(max)

if __name__ == "__main__":
    main()
