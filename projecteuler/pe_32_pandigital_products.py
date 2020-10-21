from utils.decorators import timer
"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""

def is_pandigital(n):
  str_n = str(n)
  if len(str_n) > 9 or "0" in str_n:
    return False
  for i in range(1, len(str_n)+1):
    if str_n.count(str(i)) != 1:
      return False
  return True

def pandigital_products(digits):
    max_iter = 10 ** (digits // 2)
    products = set()
    for a in range(1,max_iter):
        for b in range(1,max_iter):
            num = str(a)+str(b)+str(a*b)
            if len(num) > digits:
                break
            if len(num) == digits and is_pandigital(int(num)):
                products.add(a*b)
    return products


@timer
def main():
    print(sum(pandigital_products(9)))


if __name__ == "__main__":
    main()