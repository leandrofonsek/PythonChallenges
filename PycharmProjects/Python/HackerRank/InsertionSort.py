#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    lastNumber = arr[n - 1]
    for i in reversed(range(n - 1)):
        if arr[i] > lastNumber:
            arr[i + 1] = arr[i]
        else:
            arr[i + 1] = lastNumber
            break
        print(' '.join(map(str, arr)))
    if arr[0] > lastNumber:
        arr[0] = lastNumber
    print(' '.join(map(str, arr)))


if __name__ == '__main__':
    arr = [ 1, 3, 4, 5, 6, 7, 8, 9, 10, 2 ]
    insertionSort1(10, arr)