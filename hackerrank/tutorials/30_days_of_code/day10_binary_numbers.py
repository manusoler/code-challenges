#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    binary = "{:b}".format(n)
    matches = re.findall(r"1+", binary)
    print(max(map(len, matches)))