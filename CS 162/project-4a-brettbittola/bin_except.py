# Author:  Brett Bittola
# GitHub username: brettbittola
# Date: 10/17/2023
# Description: Binary search function that returns a TargetNotFound exception if target not found.


class TargetNotFound(Exception):
    """Error that is raised when an item is not found using binary search"""
    pass


def bin_except(a_list, target):
    """Searches a_list for an occurrence of target. If found, returns the index of its position in the list.
    If not found, returns TargetNotFound error, indicating the target value isn't in the list."""
    first = 0
    last = len(a_list) - 1
    while first <= last:
        middle = (first + last) // 2
        if a_list[middle] == target:
            return middle
        if a_list[middle] > target:
            last = middle - 1
        else:
            first = middle + 1
    raise TargetNotFound()
