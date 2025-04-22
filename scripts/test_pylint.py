"""This module implements a Caesar cipher for encoding and decoding text."""

import string

def caesar_cipher():
    """Encodes or decodes a message based on user input."""
    shift = 3
    choice = input("Would you like to encode or decode? ").lower()
    word = input("Please enter text: ")
    letters = string.ascii_letters + string.punctuation + string.digits
    encoded = ""

    if choice == "encode":
        for letter in word:
            if letter == " ":
                encoded += " "
            else:
                index = letters.index(letter) + shift
                encoded += letters[index]
    elif choice == "decode":
        for letter in word:
            if letter == " ":
                encoded += " "
            else:
                index = letters.index(letter) - shift
                encoded += letters[index]
    else:
        print("Invalid choice.")
        return

    print(encoded)

if __name__ == "__main__":
    caesar_cipher()
