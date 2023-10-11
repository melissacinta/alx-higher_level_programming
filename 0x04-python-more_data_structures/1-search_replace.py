#!/usr/bin/python3
def search_replace(my_list, search, replace):
    '''
    function to replace the search element with the replace element in my_list
    '''
    new_list = []
    for i in my_list:
        if i == search:
            new_list.append(replace)
        else:
            new_list.append(i)
    return new_list
