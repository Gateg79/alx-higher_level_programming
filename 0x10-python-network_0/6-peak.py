#!/usr/bin/python3
"""This function finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """finds the peak in a list of unsorted integers"""

    start, end = 0, len(list_of_integers) - 1
    if len(list_of_integers) == 0:
        return None
    while start < end:
        mid = start + (end - start) // 2

        # Check if it's a peak
        if list_of_integers[mid] > list_of_integers[mid - 1] and\
                list_of_integers[mid] > list_of_integers[mid + 1]:
            return list_of_integers[mid]
        if list_of_integers[mid - 1] > list_of_integers[mid + 1]:
            end = mid
        else:
            start = mid + 1
    return list_of_integers[start]
