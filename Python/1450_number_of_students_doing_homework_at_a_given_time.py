#!/usr/bin/env python3

def main() -> None:
    startTime = list(map(int, input("Enter startTime: ").split(",")))
    endTime = list(map(int, input("Enter endTime: ").split(",")))
    queryTime = int(input("Enter queryTime: "))

    num = 0

    for start, end in zip(startTime, endTime):
        if start <= queryTime and queryTime <= end:
            num += 1

    print(num)

if __name__ == "__main__":
    main()
