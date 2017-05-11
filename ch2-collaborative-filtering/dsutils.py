#!/usr/bin/env python3

"""
    This module consists of various data structure tools
"""

import collections

def sort_dict(d):
    """
        Sort the dict by keys
    """
    res = {}
    od = collections.OrderedDict(sorted(d.items()))
    return dict(od)

def convert_to_sparse(dict1, dict2):
    """
        Convert the dict to sparse.
        Each returned dicitonary contains null/0 values for the keys that
        are only found in the other dict
    """
    for key in dict2:
        if key not in dict1:
            dict1[key] = 0

    for key in dict1:
        if key not in dict2:
            dict2[key] = 0
    dict1 = sort_dict(dict1)
    dict2 = sort_dict(dict2)
    return dict1, dict2

def main():
    d1 = {'a' : 0, 'b' : 1}
    d2 = {'c': 3, 'd' : 4}
    c1, c2 = convert_to_sparse(d1, d2)
    print(c1, c2)

if __name__ == "__main__":
    main()

