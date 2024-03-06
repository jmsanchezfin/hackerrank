from math import isqrt

def is_prime(n: int) -> bool:
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    limit = isqrt(n)
    for i in range(5, limit+1, 6):
        if n % i == 0 or n % (i+2) == 0:
            return False
    return True


""""
def isPrime (data):
    count = 0
    for divisor in range(1, data):
        if data % divisor == 0:
            count = count + 1

    if count > 2 or data == 1:
        print("Not prime")
    else:
        print("Prime")

"""

T=int(input())
arr = []
for i in range(T):
    arr.append(int(input()))
for number in arr:
    print("Prime") if is_prime(number) else print("Not prime")
    

    


