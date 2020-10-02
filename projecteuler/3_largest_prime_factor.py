from math import sqrt
from itertools import count
"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(sqrt(n)), 2):
        if n % i == 0:
            return False
    return True


def prime_iter():
    for i in count(2):
        if is_prime(i):
            yield i


def prime_factors(n):
    factors = []
    num = n
    for p in prime_iter():
        while num % p == 0:
            num /= p
            factors.append(p)
        if num == 1:
            break
    return factors


if __name__ == "__main__":
    print(prime_factors(600851475143))
