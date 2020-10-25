#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    users = []
    for N_itr in range(N):
        firstNameEmailID = input().split()
        firstName = firstNameEmailID[0]
        emailID = firstNameEmailID[1]
        if re.match(r".+@gmail.com", emailID):
            users.append(firstName)
    users.sort()
    for u in users:
        print(u)