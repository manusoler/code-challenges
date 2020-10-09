#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    maxx = -1000
    for x in range(len(arr) - 2):
        for y in range(len(arr[x]) - 2):
            s = arr[x][y] + arr[x][y+1] + arr[x][y+2] + arr[x+1][y+1] + arr[x+2][y] + arr[x+2][y+1] + arr[x+2][y+2]
            maxx = s if s > maxx else maxx
    print(maxx)
