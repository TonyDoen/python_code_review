# -*- coding:utf8 -*-

import math

def isprime(n):
    if n < 2:
        return False
    
    upper = math.sqrt(n)
    k = 2 
    while k <= upper:
        if n%k == 0:
            return False
        k += 1 
    return True

arr = [x for x in range(100) if isprime(x) ]
for i, d in enumerate(arr):
    print i, d

