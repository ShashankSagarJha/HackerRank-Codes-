#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findMedian function below.
def findMedian(arr):
    sorted_arr=sorted(arr)
    size=len(arr)
    if size%2==1:
        return sorted_arr[size//2]
    return (sorted_arr[(size//2)+1]+sorted_arr[(size//2)])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr)

    fptr.write(str(result) + '\n')

    fptr.close()