#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':

    def getHourGlassSum(matrix, row, col):
        sum = 0
        sum += matrix[row-1][col-1]
        sum += matrix[row-1][col]
        sum += matrix[row-1][col+1]
        sum += matrix[row][col]
        sum += matrix[row+1][col-1]
        sum += matrix[row+1][col]
        sum += matrix[row+1][col+1]
        return sum
    
    arr = []

    #input array values
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    max_hourglass = -63
    for i in range(1,5):
        for j in range(1,5):
            current_sum = getHourGlassSum(arr, i, j)
            if current_sum > max_hourglass:
                max_hourglass = current_sum

    print(max_hourglass)
