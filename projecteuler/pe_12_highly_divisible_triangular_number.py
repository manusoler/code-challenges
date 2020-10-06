import itertools

from utils.decorators import timer
"""
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
"""

def triangle_numer_iter():
    for n in itertools.count(1):
        yield sum(range(n+1))


def factors(n):
    #return [i for i in range(1,n+1) if n % i == 0]
    fact = set()
    i, top = 1, n
    while i < top:
        if n % i == 0:
            fact.update({i, n//i})
            top = n//i
        i += 1
    return fact


def highly_divisible_triangular_number(n):
    for t in triangle_numer_iter():
        if len(factors(t)) >= n:
            return t


@timer
def main():
    print(highly_divisible_triangular_number(500))


if __name__ == "__main__":
    main()