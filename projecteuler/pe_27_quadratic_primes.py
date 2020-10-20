from math import sqrt
from itertools import count
from utils.decorators import timer
"""
Euler discovered the remarkable quadratic formula: n**2 + n + 41


It turns out that the formula will produce 40 primes for the consecutive integer values . However, when  is divisible by 41, and certainly when  is clearly divisible by 41.

The incredible formula  was discovered, which produces 80 primes for the consecutive values . The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

, where  and 

where  is the modulus/absolute value of 
e.g.  and 
Find the product of the coefficients,  and , for the quadratic expression that produces the maximum number of primes for consecutive values of , starting with .
"""

def quadratics(a,b,n):
    return n**2 + a*n + b


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(sqrt(n))+1, 2):
        if n % i == 0:
            return False
    return True


def max_consecutive_primes():
    max_consecutive, a_max, b_max, n_max = 0, 0, 0, 0
    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            consecutive = 0
            for n in count():
                if is_prime(quadratics(a,b,n)):
                    consecutive += 1
                else:
                    if consecutive > max_consecutive:
                        a_max, b_max, n_max = a, b, n - 1
                        max_consecutive = consecutive
                        #print(a, b, n - 1, consecutive)
                    break
    return (a_max, b_max, n_max, max_consecutive)


@timer
def main():
    a,b,n,consecutives = max_consecutive_primes()
    print("a: {}, b: {}, n: {}, num_consecutives: {} -> coef_product: {}".format(a,b,n,consecutives,a*b))


if __name__ == "__main__":
    main()
