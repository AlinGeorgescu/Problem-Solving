#!/usr/bin/env python3

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.__spots = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        self.__spots[carType - 1] -= 1
        if self.__spots[carType - 1] < 0:
            return False

        return True
