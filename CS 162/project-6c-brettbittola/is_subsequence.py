# Author:  Brett Bittola
# GitHub username: brettbittola
# Date: 11/3/2023
# Description: A recursive function that compares two strings and returns True if the first one is a subset of the
#              second one.

def is_subsequence(str1, str2, pos_str1=0, pos_str2=0):
    """Recursive function that returns true if string 1 is a subset of string 2"""
    if pos_str1 == len(str1):
        return True
    elif pos_str2 == len(str2):
        return False
    elif str2[pos_str2] == str1[pos_str1]:
        return is_subsequence(str1, str2, pos_str1 + 1, pos_str2 + 1)
    else:
        return is_subsequence(str1, str2, pos_str1, pos_str2 + 1)
