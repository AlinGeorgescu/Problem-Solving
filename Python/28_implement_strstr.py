#!/usr/bin/env python3

def computeLPSArray(needle, index_needle, lps):
    length = 0
    lps[0] = 0
    i = 1

    while i < index_needle:
        if needle[i]== needle[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length-1]
            else:
                lps[i] = 0
                i += 1

def main() -> None:
    haystack = input("Enter haystack: ")
    needle = input("Enter needle: ")

    len_haystack = len(haystack)
    len_needle = len(needle)

    lps = [0] * len_needle
    index_needle = 0

    computeLPSArray(needle, len_needle, lps)

    index_haystack = 0
    while index_haystack < len_haystack:
        if needle[index_needle] == haystack[index_haystack]:
            index_haystack += 1
            index_needle += 1

        if index_needle == len_needle:
            print(index_haystack - index_needle)
            return

        if index_haystack < len_haystack and needle[index_needle] != haystack[index_haystack]:
            if index_needle != 0:
                index_needle = lps[index_needle - 1]
            else:
                index_haystack += 1

if __name__ == "__main__":
    main()
