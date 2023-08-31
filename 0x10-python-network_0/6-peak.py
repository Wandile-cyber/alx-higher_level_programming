#!/usr/bin/python3
"""
Find a peak element in the list of integers.

Parameters:
list_of_integers (list): List of unsorted integers

Returns: 
int: Peak element value

"""

if len(list_of_integers) == 1:
    return list_of_integers[0]
    
mid = len(list_of_integers) // 2
mid_value = list_of_integers[mid]   

"""
If middle element is greater than neighbors, it is a peak
Otherwise recursively search left or right half
"""

if mid_value > list_of_integers[mid-1] and mid_value > list_of_integers[mid+1]:
    return mid_value

if mid_value < list_of_integers[mid-1]:  
    return find_peak(list_of_integers[:mid])

return find_peak(list_of_integers[mid:])
