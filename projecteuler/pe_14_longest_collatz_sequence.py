import os
from utils.decorators import timer
"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

def collatz_seq(n):
    seq_n = 0
    while n > 1:
        n = n//2 if n % 2 == 0 else 3*n+1
        seq_n += 1
    return seq_n


def longest_collatz_seq(n):
    num, maxx = 0, 0
    for i in range(2, n):
        seq_n = collatz_seq(i)
        if seq_n > maxx:
            num = i
            maxx = seq_n
    return num, maxx

@timer
def main():
    print(longest_collatz_seq(1000000))


if __name__ == "__main__":
    main()