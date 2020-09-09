#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the theLoveLetterMystery function below.
def theLoveLetterMystery(s):
    size=len(s)
    result=0
    if size==0 or size==1:
        return 0
    for i in range(size):
        if i>(size-i-1) or i==(size-i-1):
            break
        result+=abs(ord(s[i])-ord(s[size-i-1]))
    return result



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        fptr.write(str(result) + '\n')

    fptr.close()
