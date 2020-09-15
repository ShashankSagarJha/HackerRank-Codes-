#!/bin/python3

import math
import os
import random
import re
import sys
# Complete the superDigit function below.
def superDigit(n, k):
    n=str(n)
    if len(n)==1:
        return n
    summ=0
    for i in n:
        summ+=int(i)
    if k>1:
        summ*=k
    return superDigit(summ, 1)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
