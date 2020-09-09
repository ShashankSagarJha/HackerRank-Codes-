#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the funnyString function below.
def funnyString(s):
    r_s=s[::-1]
    s_list=[]
    r_list=[]
    for i in s:
        s_list.append(ord(i))
    for j in r_s:
        r_list.append(ord(j))   
    
    r_diff=[]
    s_diff=[]
    for k in range(0,len(s)-1):
        r_diff.append(abs(r_list[k]-r_list[k+1]))
        s_diff.append(abs(s_list[k]-s_list[k+1])) 
    
    return "Funny" if r_diff==s_diff else "Not Funny"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()