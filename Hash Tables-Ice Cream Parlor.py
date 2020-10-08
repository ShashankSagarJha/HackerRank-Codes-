#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    mapped={}
    for index,val in enumerate(cost):
        if val in mapped.keys():
            print(mapped[val],index+1)
            return
        else:
            mapped[money-val]=index+1

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
