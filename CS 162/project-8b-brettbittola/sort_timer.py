# Author:  Brett Bittola
# GitHub username: brettbittola
# Date: 11/15/2023
# Description: Compares the time it takes to sort increasing lists of data using bubble sort and insertion sort

import time
import random
from matplotlib import pyplot
import functools


def sort_timer(func):
    """Adds timers before and after a function runs"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        pre_time = time.perf_counter()
        func(*args, **kwargs)
        post_time = time.perf_counter()
        total_time = post_time - pre_time
        return total_time
    return wrapper


@sort_timer
def bubble_sort(a_list):
    """Sorts a list in ascending order using bubble sort"""
    for pass_num in range(len(a_list) - 1):
        for index in range(len(a_list) - 1 - pass_num):
            if a_list[index] > a_list[index + 1]:
                temp = a_list[index]
                a_list[index] = a_list[index + 1]
                a_list[index + 1] = temp


@sort_timer
def insertion_sort(a_list):
    """Sorts a list in ascending order using insertion sort"""
    for index in range(1, len(a_list)):
        value = a_list[index]
        pos = index - 1
        while pos >= 0 and a_list[pos] > value:
            a_list[pos + 1] = a_list[pos]
            pos -= 1
        a_list[pos + 1] = value


def make_lists_of_sort_times(sort_func1, sort_func2, length_list):
    """Creates two lists of sorting algorithm times"""
    func1_list = []
    func2_list = []
    for num in length_list:
        list_1 = [random.randint(1, 10000) for item in range(num)]
        list_2 = list(list_1)
        func1_list.append(sort_func1(list_1))
        func2_list.append(sort_func2(list_2))
    return func1_list, func2_list


def compare_sorts(dec_sort_func1, dec_sort_func2):
    """Compares a plot comparing the two lists of sort times"""
    function_times = make_lists_of_sort_times(dec_sort_func1, dec_sort_func2, [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000])
    func1_times = function_times[0]
    func2_times = function_times[1]
    pyplot.plot([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000], func1_times, 'ro--', linewidth=2, label='Bubble sort')
    pyplot.plot([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000], func2_times, 'go--', linewidth=2, label='Insertion sort')
    pyplot.xlabel("Number of elements being sorted")
    pyplot.ylabel("Time in seconds")
    pyplot.legend(loc='upper left')
    pyplot.show()


compare_sorts(bubble_sort, insertion_sort)
