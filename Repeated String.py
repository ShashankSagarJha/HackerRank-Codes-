#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    size=len(s)
    if "a" not in s:
        return 0
    if size==1 and s[0]=="a":
        return n
    counter=0;pos=[]
    for i in s:
        if i=="a":
            counter+=1
            pos.append(1)
        else:
            pos.append(0)
    counter*=(n//size)
    mod=(n%size)
    return counter+sum(pos[0:mod])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
