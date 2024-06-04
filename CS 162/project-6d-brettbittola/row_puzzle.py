# Author:  Brett Bittola
# GitHub username: brettbittola
# Date: 11/6/2023
# Description: Recursive function that takes a list of numbers and returns True if the last zero can be reached only
#              by moving the number of spaces equal to the value in its current space

def row_puzzle(num_list, pos=0, row_puzzle_cache=None):
    """Takes a list of numbers and returns True if the last zero can be reached only by moving the number of spaces
    equal to the value in its current space"""
    if row_puzzle_cache is None:
        row_puzzle_cache = []
    if pos not in row_puzzle_cache:
        if pos == (len(num_list) - 1):
            return True
        else:
            row_puzzle_cache.append(pos)
        try:
            pos += num_list[pos]
            if 0 <= pos < len(num_list):
                if row_puzzle(num_list, pos, row_puzzle_cache):
                    return True
        except IndexError:
            pass

        try:
            pos -= num_list[pos]
            if 0 < pos < len(num_list):
                if row_puzzle(num_list, pos, row_puzzle_cache):
                    return True
        except IndexError:
            pass
    return False
