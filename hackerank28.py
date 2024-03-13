#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    
    arr = []

    N = int(input().strip())

    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()

        firstName = first_multiple_input[0]

        emailID = first_multiple_input[1]

        isGmail = re.search('@gmail.com', emailID)

        if isGmail:
            arr.append(firstName)
    arr.sort()
    print(*arr, sep='\n')