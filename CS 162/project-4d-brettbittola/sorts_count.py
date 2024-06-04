# Author:  Brett Bittola
# GitHub username: brettbittola
# Date: 10/17/2023
# Description: Returns a tuple containing how many comparisons and exchanges occurred for a bubble sort and an
#              insertion sort function.

def bubble_count(a_list):
    """Sorts a list in ascending order, and counts the number of comparisons and exchanges it makes"""
    comparisons = 0
    exchanges = 0
    for pass_num in range(len(a_list) - 1):
        for index in range(len(a_list) - 1 - pass_num):
            comparisons += 1
            if a_list[index] > a_list[index + 1]:
                temp = a_list[index]
                a_list[index] = a_list[index + 1]
                exchanges += 1
                a_list[index + 1] = temp
    return comparisons, exchanges


def insertion_count(a_list):
    """Sorts a list in ascending order, and counts the number of comparisons and exchanges it makes"""
    comparisons = 0
    exchanges = 0
    for index in range(1, len(a_list)):
        value = a_list[index]
        pos = index - 1
        while pos >= 0 and a_list[pos] > value:
            a_list[pos + 1] = a_list[pos]
            comparisons += 1
            exchanges += 1
            pos -= 1
        a_list[pos + 1] = value
    return comparisons, exchanges
