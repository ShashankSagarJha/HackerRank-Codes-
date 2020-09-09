#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pangrams function below.
def pangrams(s):
    char_list=[]
    for i in range(97,123):
        char_list.append(chr(i))
        for i in char_list:
            if i not in s.lower():
                return "not pangram"
    return "pangram"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()