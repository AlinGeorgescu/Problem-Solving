#!/usr/bin/env python3

from math import floor, log

def main() -> None:
    address = input("Enter an IP address: ")
    address = address.split(".")
    address = "[.]".join(address)

    print("Resulted IP: " + address)

if __name__ == "__main__":
    main()
