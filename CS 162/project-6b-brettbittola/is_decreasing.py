# Author:  Brett Bittola
# GitHub username: brettbittola
# Date: 11/3/2023
# Description: Recursive function that determines if a given list of numbers are in decreasing order.

def is_decreasing(num_list):
    """Determines if a given list of numbers are in decreasing order"""
    if len(num_list) == 1:
        return True
    elif num_list[-1] < num_list[-2]:
        return is_decreasing(num_list[:-1])
    else:
        return False
