# Author:  Brett Bittola
# GitHub username: brettbittola
# Date: 10/17/2023
# Description: Sorts a list of strings, ignoring case, using insertion sort.


def string_sort(string_list):
    """Sorts a list of strings in ascending order, ignoring case"""
    for index in range(1, len(string_list)):
        value = string_list[index]
        pos = index - 1
        while pos >= 0 and string_list[pos].lower() > value.lower():
            string_list[pos + 1] = string_list[pos]
            pos -= 1
        string_list[pos + 1] = value
