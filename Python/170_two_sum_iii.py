#!/usr/bin/env python3

class TwoSum:
    def __init__(self):
        self.items = {}

    def add(self, number: int) -> None:
        if number in self.items:
            self.items[number] += 1
        else:
            self.items[number] = 1

    def find(self, value: int) -> bool:
        for item, occurences in self.items.items():
            if value - item == item:
                if occurences > 1:
                    return True
            elif value - item in self.items:
                return True

        return False

def main() -> None:
    structure = TwoSum()
    structure.add(1)
    structure.add(3)
    structure.add(5)

    print(structure.find(4), structure.find(7))

    structure = TwoSum()
    structure.add(3)
    structure.add(1)
    structure.add(2)

    print(structure.find(3), structure.find(6))

    structure = TwoSum()
    structure.add(3)
    structure.add(3)
    structure.add(2)

    print(structure.find(3), structure.find(6))


if __name__ == "__main__":
    main()