#!/bin/python3

import sys

n = int(input().strip())
array = list(map(int, input().strip().split(' ')))
# Write Your Code Here

def bubble_sort(array):
    swapCount = 0
    for n in range(len(array)-1, 0, -1):

        for i in range(n):

            if array[i] > array[i+1]:
                swapCount += 1
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp

    print('Array is sorted in {} swaps.'.format(swapCount))
    print('First Element: {}'.format(array[0]))
    print('Last Element: {}'.format(array[-1]))


bubble_sort(array)
