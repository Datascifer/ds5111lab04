"""This module implements a Caesar cipher for encoding and decoding text."""

import string

LETTERS = string.ascii_letters + string.punctuation + string.digits
SHIFT = 3

def encode(text):
    """Encodes text using Caesar cipher"""
    result = ""
    for char in text:
        if char == " ":
            result += " "
        else:
            index = LETTERS.index(char) + SHIFT
            result += LETTERS[index]
    return result

def decode(text):
    """Decodes text using Caesar cipher"""
    result = ""
    for char in text:
        if char == " ":
            result += " "
        else:
            index = LETTERS.index(char) - SHIFT
            result += LETTERS[index]
    return result
