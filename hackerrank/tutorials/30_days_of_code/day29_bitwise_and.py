#!/bin/python3

import math
import os
import random
import re
import sys

def get_nks(n,k):
    if k < n:
        for ki in reversed(range(1,k)):
            for a in range(ki, n):
                for b in range(a+1, n+1):
                    if a & b == ki:
                        return ki
    return 0

def solution(nks):
    for n, k in nks:
        print(get_nks(n, k))

if __name__ == '__main__':
    t = int(input())
    nks = []
    for t_itr in range(t):
        nk = input().split()
        n = int(nk[0])
        k = int(nk[1])
        nks.append((n,k))
    solution(nks)