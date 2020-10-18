#!/bin/python3

import sys

def bubble_sort(array):
    n = len(array)
    num_swaps = 0
    for i in range(n):
        for j in range(n-1):
            if array[j] > array[j+1]:
                swap(array, j, j+1)
                num_swaps += 1
        if not num_swaps:
            break
    return num_swaps

def swap(array, pos1, pos2):
    tmp = array[pos1]
    array[pos1] = array[pos2]
    array[pos2] = tmp

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
swaps = bubble_sort(a)
print("Array is sorted in {} swaps.".format(swaps))
print("First Element: {}".format(a[0]))
print("Last Element: {}".format(a[-1]))
