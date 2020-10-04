import itertools
import functools
from .pe_3_largest_prime_factor import prime_factors
"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


def smallest_common_divisor(*nums):
    # 1. Find all the prime factor for each number
    factors = []
    for i in nums:
        factors.append(prime_factors(i))
    # 2. Get Max repetions of each prime in every factor
    # Divisors now contains each prime
    divisors = dict.fromkeys(itertools.chain.from_iterable(factors), 0)
    for p in divisors.keys():
        for f in factors:
            divisors[p] = f.count(p) if divisors.get(
                p) < f.count(p) else divisors[p]
    # 3. Multiple them
    return functools.reduce(lambda x, y: x*y, [k**v for k, v in divisors.items()])


def main():
    print(smallest_common_divisor(*range(1, 21)))


if __name__ == "__main__":
    main()
