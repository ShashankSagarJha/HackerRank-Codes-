#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    e=100
    size=len(c)
    i=0
    while (i+k)%size!=0:
        z=(i+k)%size
        if c[z]!=0:
            e-=3
        else:
            e-=1
        i+=k
        
    return e-1 if c[0]==0 else e-3

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
