import functools
from utils.decorators import timer
"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

def factorial(n):
    sol = n
    for i in range(1,n):
        sol *= i
    return sol


def factorial_digit_sum(n):
    return functools.reduce(lambda x,y: int(x)+int(y), str(factorial(n)))


@timer
def main():
    print(factorial_digit_sum(100))


if __name__ == "__main__":
    main()