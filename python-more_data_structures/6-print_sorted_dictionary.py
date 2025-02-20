#!/usr/bin/python3

# Function to print dictionary keys in sorted order


def print_sorted_dictionary(a_dictionary):
    for key in sorted(a_dictionary):
        print(f"{key}: {a_dictionary[key]}")
