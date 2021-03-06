import functools
from utils.decorators import timer
"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

def divisors(n):
    return [i for i in range(1,n) if n % i == 0]


def amicable(n):
    b = sum(divisors(n))
    a = sum(divisors(b))
    return b if a == n and a != b else None


def get_amicables_in_range(n):
    amicables = []
    for i in range(1, n):
        if i not in amicables:
            amic = amicable(i)
            if amic:
                #amicables.append((i,amic))
                amicables.extend([i,amic])
    return amicables

@timer
def main():
    amicables = get_amicables_in_range(10000)
    print(sum(amicables))

if __name__ == "__main__":
    main()