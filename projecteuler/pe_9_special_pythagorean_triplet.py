import functools
from math import sqrt

from utils.decorators import timer
"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a**2+b**2=c**2
a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


def pythagorean_triplet(summ):
    for a in range(1,summ):
        for b in range(a+1, summ):
            c = sqrt(a**2+b**2)
            if a + b + c == summ:
                return (a,b,int(c))

@timer
def main():
    triplet = pythagorean_triplet(1000)
    print("Triplet: {}, Product: {}".format(triplet, functools.reduce(lambda x,y: x*y, triplet)))


if __name__ == "__main__":
    main()
