#!/bin/python3

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    
    for i in range(n):
        print(arr[n-i-1], end= " ") # -1 for starting position