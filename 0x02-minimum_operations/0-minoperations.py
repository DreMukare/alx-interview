#!/usr/bin/python3
'''module contains solution to min-operations problem'''
import math


def highestPrimeFactor(n):
    '''finds highest prime factor of n'''
    max_prime = 0

    while n % 2 == 0:
        max_prime = 2
        n = n / 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            max_prime = i
            n = n / i

    if n > 2:
        max_prime = n

    return int(max_prime)


def isPrime(n):
    ''' checks whether number is prime or not '''
    flag = False

    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                flag = True
                break
    return not flag


def minOperations(n):
    ''' finds number of minimum of operations to get n number of H '''
    if n <= 1:
        return 0

    if n == 2 or isPrime(n):
        return n

    hpf = highestPrimeFactor(n)
    resultOfDivision = n / hpf
    return int(hpf + resultOfDivision)
