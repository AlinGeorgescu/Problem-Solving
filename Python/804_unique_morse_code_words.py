#!/usr/bin/env python3

def main() -> None:
    MORSE = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..",
             ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.",
             "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

    seen = {"".join(MORSE[ord(c) - ord('a')] for c in word) for word in words}

    print(len(seen))

if __name__ == "__main__":
    main()
