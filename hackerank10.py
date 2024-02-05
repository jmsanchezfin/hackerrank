#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    #take decimal input and convert it to binary

    stack = []

    while(n > 0):
        remainder = n%2;
        n = int(n/2)
        stack.append(remainder)
    print(stack)

    #count how many consecutive 1's in stack
    max = 0
    count = 0
    for item in stack:
        if item == 1:
            count = count + 1
        else:
            count = 0
        if count > max:
            max = count
            
    print(max)