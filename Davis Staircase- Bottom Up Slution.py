#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the stepPerms function below.
def stepPerms(n):
    my_dict={1:1,2:2,3:4}
    for i in range(4,n+1):
        my_dict[i]=my_dict[i-1]+my_dict[i-2]+my_dict[i-3]
    return my_dict[n]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input())

    for s_itr in range(s):
        n = int(input())

        res = stepPerms(n)

        fptr.write(str(res) + '\n')

    fptr.close()