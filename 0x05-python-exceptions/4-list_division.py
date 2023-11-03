#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """prints the first x elements of a list and only integers

    Args:
        my_list_1(list): can contain any type (integer, string, etc.)
        my_list_2(list): can contain any type (integer, string, etc.)
        list_length(int): number of elements to access in my_list

    Returns:
        new list (length = list_length) with all divisions
    """
    new_list = []
    for i in range(0, list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            result = 0
            print("wrong type")
        except ZeroDivisionError:
            result = 0
            print("division by 0")
        except IndexError:
            result = 0
            print("out of range")
        finally:
            new_list.append(result)

    return new_list
