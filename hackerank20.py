import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    # Write your code here

    numSwaps = 0
    totalSwaps = 0
    
    #traverse each position once
    for pos in range(n):
        totalSwaps = totalSwaps + numSwaps
        numSwaps = 0

        # traverse through array and order positions to max last
        for i in range(n-1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                numSwaps += 1
        if numSwaps == 0:
            break
            
    print('Array is sorted in', totalSwaps, 'swaps.')
    print('First Element:', a[0])
    print('Last Element:', a[n-1])

    