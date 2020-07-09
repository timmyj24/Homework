# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 10:47:09 2020

@author: tleta
"""


#!/bin/python

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    #initializing variables
    clouds = c                  #binary list
    jumps = 0
    cloud = 0
    finished = False
    #creating a loop to iterate through the list
    while finished == False:
        #can take a 'greedy approach' and always try to move forward two spaces
        #following line checks if there is space to move two and if two ahead is safe
        if  cloud < len(clouds)-2 and clouds[cloud+2] == 0:
            jumps += 1                      #counting a jump
            cloud += 2                      #tracking my current cloud
        elif cloud < len(clouds)-1:         #checking that they are not on the final cloud
            jumps += 1
            cloud += 1
        else:
            finished = True
    return jumps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    c = map(int, raw_input().rstrip().split())

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
