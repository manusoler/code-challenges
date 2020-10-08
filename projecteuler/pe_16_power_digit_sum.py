import functools
from utils.decorators import timer
"""
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?
"""

def power_digit_sum(n):
    return functools.reduce(lambda x,y: int(x)+int(y), str(2**n))


@timer
def main():
    print(power_digit_sum(1000))


if __name__ == "__main__":
    main()