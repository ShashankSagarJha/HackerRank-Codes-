#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the balancedSums function below.
def balancedSums(arr):
    sum_left=[]
    sum_right=[]
    summed_left=0
    for ind,val in enumerate(arr):
        sum_left.append(summed_left+val)
        summed_left+=val
    summed_right=0
    for ind in range(len(arr)-1,-1,-1):
        sum_right.append(summed_right+arr[ind])
        summed_right+=arr[ind]
    sum_right=sum_right[::-1]
    for i,v in enumerate(arr):
        if sum_left[i]==sum_right[i]:
            return "YES"
    return "NO"    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()
