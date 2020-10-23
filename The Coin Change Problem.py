#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getWays' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. LONG_INTEGER_ARRAY c
#
coin_dict={}
def getWays(n, c):
    size=len(c)
    try:
        return coin_dict[(n,size)]
    except KeyError:
        if n<0:return 0
        if n==0:return 1;
        counter=0
        for i,val in enumerate(c):
            counter+=getWays(n-val,c[i:])
        coin_dict[(n,size)]=counter
        return counter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    ways = getWays(n, c)

    fptr.write(str(ways) + '\n')

    fptr.close()
