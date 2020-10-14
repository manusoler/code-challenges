import functools
from utils.decorators import timer
"""
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

def nth_permutation(elems, n):
    """
    Find nth lexicographic permutation of elems by calculating 
    the number of permutatios left for each position
    elems array with elements to permutate, must be sorted
    n the nth lexicographic permutation to find
    """
    fact = lambda x: functools.reduce(lambda i,j: i*j, range(1,x+1))
    pos, summ = 0, 0
    permutation = ""
    for i in reversed(range(1,len(elems))):
        fact_i = fact(i)
        while summ+fact_i < n:
            summ += fact_i
            pos += 1
        permutation += str(elems[pos])
        del(elems[pos])
        pos = 0
    return permutation + str(elems[0])


@timer
def main():
    print(nth_permutation([i for i in range(0,10)], 1000000))
    

if __name__ == "__main__":
    main()