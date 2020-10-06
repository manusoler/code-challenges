from math import sqrt
from itertools import count

from utils.decorators import timer
"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""


def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(sqrt(n))+1, 2):
        if n % i == 0:
            return False
    return True


def prime_iter():
    for i in count(2):
        if is_prime(i):
            yield i

def nth_prime(n):
    i = 1
    for p in prime_iter():
        if i == n:
            return p
        i += 1


@timer
def main():
    print(nth_prime(10001))


if __name__ == "__main__":
    main()
