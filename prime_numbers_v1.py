#!/usr/local/bin/python

import math
import time

def isPrime(num):
    if num <= 0:
        print("El numero tiene que ser mayor a 1")
        return False
    if num == 1:
        return False
    if num == 2:
        return True
    if num > 2 and num % 2 == 0:
        return False

    max_divisor = math.floor(math.sqrt(num))
    for d in range(3, 1 + max_divisor, 2):
        if num % d == 0:
            return False
    return True

print(isPrime(0))
print(isPrime(2))
print(isPrime(3))
print(isPrime(37))
print(isPrime(1))
print(isPrime(1800))
print(isPrime(115200))
