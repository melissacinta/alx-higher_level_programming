#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x elements in a list

    Args:
        my_list(list): contains a list of any type
        x(int): number of elements to print.

    Returns:
        the number of elements printed
    """
    count = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            count += 1
        except IndexError:
            break
    print("")
    return count
