"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def multiples_of(*nums, max=1000):
    return [i for i in range(max) if any([i % n == 0 for n in nums])]

if __name__ == "__main__":
    print(sum(multiples_of(3,5)))
