import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

i = 0
while i < 10:
    i += 1
    print(n, 'x', i, '=', n*i, sep=' ')