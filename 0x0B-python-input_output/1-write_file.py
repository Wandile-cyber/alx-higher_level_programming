#!/usr/bin/python3
"""Python Function that reads a file and prints to stdout""" 


def read_file(filename=""):
    """Reading a file using with""" 
    with open(filename, encoding='utf-8') as f:
        for line in f:
            print(line, end="")
