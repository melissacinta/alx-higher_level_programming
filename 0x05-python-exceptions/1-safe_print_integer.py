#!/usr/bin/python3

def safe_print_integer(value):
    """prints an integer with "{:d}".format()

    Args:
        value(int): integer to print
    
    Returns:
        True - if value has been corrected printed
        otherwise returns false
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False
