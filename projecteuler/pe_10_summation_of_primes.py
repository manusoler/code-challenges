from .pe_3_largest_prime_factor import prime_iter
"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""


def summation_of_primes_below(n):
    summation = 0
    for p in prime_iter():
        if p > n:
            break
        summation += p
    return summation

def main():
    print(summation_of_primes_below(2000000))


if __name__ == "__main__":
    main()