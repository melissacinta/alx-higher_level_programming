#!/usr/bin/python3
"""Module housing a function that read file to the stdout"""


def read_file(filename=""):
  """Function to read from file and print to the stdout"""
  with open(filename, encoding="utf-8") as f:
    read_data = f.read()
    print(read_data, end='')
