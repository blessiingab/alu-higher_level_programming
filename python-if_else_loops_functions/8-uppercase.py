#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        if 'a' <= char <= 'z':  # Check if lowercase
            result += chr(ord(char) - 32)  # Convert to uppercase
        else:
            result += char  # Keep non-lowercase characters unchanged
    print(result)

