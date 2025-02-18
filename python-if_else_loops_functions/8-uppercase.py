#!/usr/bin/python3
def print_last_digit(number):
    # First print function, using string formatting
    print("Last digit: {}".format(abs(number) % 10), end="")  # Prints formatted string
    return abs(number) % 10  # Returns last digit

