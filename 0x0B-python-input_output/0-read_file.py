#!/usr/bin/python3
"""Defining a function that read a text"""


def read_file(filename=""):
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
