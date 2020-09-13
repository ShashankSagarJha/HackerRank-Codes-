#!/bin/python

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
cut_times=[]
def cutTheSticks(arr):
    if len(arr)==0:
        return cut_times
    min_value=min(arr)
    counter=0
    new_arr=[]
    for i in arr:
        if i-min_value>=0:
            counter+=1
            if  i-min_value>0:
                new_arr.append(i-min_value)
    cut_times.append(counter)
    
    return cutTheSticks(new_arr)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
