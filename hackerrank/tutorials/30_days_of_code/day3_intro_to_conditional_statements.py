#!/bin/python3

import math
import os
import random
import re
import sys

def is_weird(n):
    if n % 2 != 0 or n in range(6,21):
        return True
    return False

if __name__ == '__main__':
    N = int(input())
    print("Weird" if is_weird(N) else "Not Weird")
