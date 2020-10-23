from math import sqrt


def is_prime(n):
    if n == 2: return True
    if n < 2 or n % 2 == 0: return False
    for i in range(3,int(sqrt(n))+1,2):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    num_tests = [int(input()) for i in range(int(input()))]
    for n in num_tests:
        print("Prime" if is_prime(n) else "Not prime")