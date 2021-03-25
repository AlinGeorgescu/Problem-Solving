#!/usr/bin/env python3

from typing import List

class OrderedStream:

    def __init__(self, n: int):
        self.ptr = 1
        self.chunk = [None] * n

    def insert(self, idKey: int, value: str) -> List[str]:
        if idKey == self.ptr:
            oldPtr = self.ptr

            while self.ptr < len(self.chunk) and \
                  not self.chunk[self.ptr] is None:
                self.ptr += 1

            self.ptr += 1

            return [value] + self.chunk[oldPtr:self.ptr - 1]

        else:
            self.chunk[idKey - 1] = value

            return []
