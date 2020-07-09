# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 13:26:42 2020

@author: tleta
"""


import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    #Checking constraints
    if 1>n or n>100:
        return "Please ensure your sock pile is between 1 and 100."
    if len(ar)>n: 
        return "please ensure you don't have more colors than socks."
    Colors = set(ar)                #creating a set to see which colors are there

    pairs = 0                       #initializing the pairs variable
    for color in Colors:            #establishing the range to be iterated through
        temp = ar.count(color)     #tallying the number of each color in the set 
        pairs += temp//2          #finding the pairs and discarding the solo socks
    return pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    ar = map(int, raw_input().rstrip().split())

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
    
    """The problem had set constraints but didn't care whether or not you ran a 
    try/catch"""
    