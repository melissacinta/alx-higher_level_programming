#!/usr/bin/python3

def safe_print_division(a, b):
    """divides 2 integers and prints the result

    Args:
    a(int): integer num
    b(int): integer num

    Returns:
        the value of the division, otherwise: None
    """
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        result
    finally:
        print("Inside result: {}".format(result))

    return result
