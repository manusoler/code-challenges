"""
A palindromic number reads the same both ways. The largest palindrome 
made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def is_palindromic(n):
    return str(n) == str(n)[::-1]


def palindromic_number(digits_n):
    max_dn = 10**digits_n
    min_dn = 10**(digits_n-1)
    palindromics = []
    for n1 in reversed(range(min_dn, max_dn)):
        for n2 in reversed(range(min_dn, n1)):
            product = n1*n2
            if is_palindromic(product):
                palindromics.append(product)
    palindromics.sort()
    return palindromics[-1]

if __name__ == "__main__":
    print(palindromic_number(3))
