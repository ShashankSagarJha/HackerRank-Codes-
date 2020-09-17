#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    map_a={}
    map_b={}
    for i in a:
        if i in map_a.keys():
            map_a[i]+=1
        else:
            map_a[i]=1
    for j in b:
        if j in map_b.keys():
            map_b[j]+=1
        else:
            map_b[j]=1

    count=0
    for l in map_a.keys():
        if l in map_b.keys():
            count+=abs(map_a[l]-map_b[l])
        else:
            count+=map_a[l]

    for k in map_b.keys():
        if k not in map_a.keys():
            count+=map_b[k]
    return count
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
