#!/usr/bin/python3

def read_file(filename=""):
  """Function to read from file and print to the stdout"""
  with open(filename, encoding="utf-8") as f:
    read_data = f.read()
    print(read_data)
