#!/usr/local/bin/python

import sys
import math
import time

def isPrime(num):
    #print(f'num on isPrime {num}')
    if num <= 0:
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

def main(args):
    #print(f'Arg on main {args}')
    if len(args) < 2:
        print("Uso: python numeros_primos_v2.py <numero>")
        print("Donde: numero es un numero entero mayor a 1")
        return

    for elem in args[1:]:
        try:
            n = int(elem)
            if n <= 1:
                print("El numero tiene que ser mayor a 1")
                continue

            if isPrime(n):
                print(f'El numero {n} es primo')
            else:
                print(f'El numero {n} no es primo')
        except:
            print(f'{elem} no es un numero entero')
            continue

if __name__ == "__main__":
    #print(sys.argv)
    main(sys.argv)

