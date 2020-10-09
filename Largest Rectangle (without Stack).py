#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the largestRectangle function below.
def largestRectangle(h):
    size=len(h)
    max_area=0
    for i in range(size):
        left_count=0
        right_count=0
        for j in range(i-1,-1,-1):
            if h[j]>=h[i]:
                left_count+=1
            else:
                break
        for j in range(i+1,size):
            if h[j]>=h[i]:
                right_count+=1
            else:
                break
        area=(1+left_count+right_count)*h[i]
        if area>max_area:
            max_area=area
    return max_area

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
