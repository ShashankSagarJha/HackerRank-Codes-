#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the missingNumbers function below.
def missingNumbers(arr, brr):
    map_arr={};map_brr={};final_list=[]
    #creating dictionary for number count in list arr
    for i in arr:
        if i in map_arr.keys():map_arr[i]+=1
        else:map_arr[i]=1
    #creating dictionary for number count in list brr
    for j in brr:
        if j in map_brr.keys():map_brr[j]+=1
        else:map_brr[j]=1
    #iterationg through list brr and checking if counts are same or not
    for i in map_brr.keys():
        if i not in map_arr.keys() or map_arr[i]!=map_brr[i]:
            final_list.append(i)
    return sorted(final_list)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
