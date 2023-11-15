# write a function that takes two lists and returns the order of elements in second list in first list
# write an efficient python function that gets a list of numbers and returns the largest subset of numbers that are in ascending order.
# for input [1, 2, 5, 7, 3, 4, 6, 11] the output should be [1, 2, 3, 4, 6, 11]
# for input [2, 4, 6, 0, 3, 8] the output should be [2, 4, 6, 8]

import sys

def mxs_order_type1(lst1, lst2):
    #initialize dict2
    dict2 = {}
    for i in lst2:
        # add lst2[i] and i to dict2 as key and value
        dict2.setdefault(i, lst2.index(i))

    lst2_index = []
    for i in lst1:
        lst2_index.append(dict2[i])
    
    return lst2_index

def mxs_order_type2(lst1, lst2):
    lst2_index = []
    for i in lst2:
        # index of lst[i] in lst1
        lst2_index.append(lst1.index(i))
    
    return lst2_index

def longest_sorted_subset