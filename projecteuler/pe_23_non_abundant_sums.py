from utils.decorators import timer
"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper 
divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. 
By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. 
However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as 
the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

def divisors(n):
    return [i for i in range(1,n//2+1) if n % i == 0]


def is_perfect(n):
    """
    0 if n is perfect
    1 if n abundant
    -1 if n is deficent
    """
    sum_divisors = sum(divisors(n))
    return 0 if sum_divisors == n else (1 if sum_divisors > n else -1)


def is_sum_of_two_elems(elem_array, n):
    """
    Check if n can be the result of the sum of any of 2 elems in elem_array
    """
    for i in elem_array:
        if i >= n:
            break
        for j in elem_array:
            if i+j > n:
                break
            elif i+j == n:
                return True
    return False
    
    
@timer
def main():
    abundants = [i for i in range(28123) if is_perfect(i) > 0]
    not_sum_from_2_abundants = [i for i in range(1,28124) if not is_sum_of_two_elems(abundants, i)]
    print(not_sum_from_2_abundants, sum(not_sum_from_2_abundants))
    

if __name__ == "__main__":
    # Takes 3174310 ms to exec |0|. Greater numbers was 20161
    main()