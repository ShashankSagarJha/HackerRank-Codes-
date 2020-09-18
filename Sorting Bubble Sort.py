#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    size=len(a)
    count=0
    for i in range(0,size):
        for j in range(i+1,size):
            if a[i]>a[j]:
                count+=1
                a[i],a[j]=a[j],a[i]
    print("Array is sorted in {} swaps.".format(count))
    print("First Element:",a[0])
    print("Last Element:",a[size-1])

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)