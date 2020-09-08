#!/bin/python3
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
    counter=s.count("a")
    counter*=(n//size)
    mod=(n%size)
    return counter+(s[0:mod]).count("a")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
