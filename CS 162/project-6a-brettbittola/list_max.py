# Author:  Brett Bittola
# GitHub username: brettbittola
# Date: 11/3/2023
# Description: Returns the maximum value in a list using recursion.

def list_max(num_list, pos=0, max_number=None):
    """Finds the maximum value in a given list of numbers"""
    if pos == len(num_list) - 1:
        return max_number
    elif max_number == None or num_list[pos] > max_number:
        max_number = num_list[pos]
        return list_max(num_list, pos + 1, max_number)
    else:
        return list_max(num_list, pos + 1, max_number)

