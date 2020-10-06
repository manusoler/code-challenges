import os
from utils.decorators import timer
"""
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
"""

@timer
def main():
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pe_13_numbers.txt'),'r') as f:
        summ = 0
        for l in f.readlines():
            summ += int(l)
        print(str(summ)[0:10])


if __name__ == "__main__":
    main()