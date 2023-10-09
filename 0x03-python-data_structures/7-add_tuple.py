#!/usr/bin/python3
'''
Function to add two tupples contain integers
'''


def add_tuple(tuple_a=(), tuple_b=()):
    list_a, list_b = list(tuple_a), list(tuple_b)
    new_list = []
    a, b = 0, 0
    for i in range(0, 2):
        if i < len(list_a):
            a = list_a[i]
        if i < len(list_b):
            b = list_b[i]
        new_list.append(a + b)
    return tuple(new_list)
