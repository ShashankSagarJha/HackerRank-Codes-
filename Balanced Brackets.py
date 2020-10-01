#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(new_s):
    stack=[]
    count=0
    for i in new_s:
        if i=="{" or i=="(" or i=="[":
            stack.append(i)
            count+=1    
        elif count!=0 and ((i==")" and stack[count-1]=="(") or (i=="}" and stack[count-1]=="{") or (i=="]" and stack[count-1]=="[")):
            stack.pop()
            count-=1
        elif count==0 and (i=="}" or i=="]" or i==")" ):
            return "NO"
        else:
            return "NO"
    return "YES" if count==0 else "NO" 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()