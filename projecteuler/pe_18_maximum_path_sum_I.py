import os
from utils.decorators import timer
"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below, 
the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. 
However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)
"""

def maximum_path_sum(piramid):
    # Build new piramid with the sum in each level of the cell value and theirs parents
    p2 = [piramid[0]]
    for depth, piramid_row in enumerate(piramid[1:], start=1):
        new_calculated_row = []
        for x, node in enumerate(piramid_row):
            if x > 0 and x < len(piramid[depth-1]):
                new_calculated_row.append(sum_check_list(
                    p2[depth-1][x-1], node) + sum_check_list(p2[depth-1][x], node))
            elif x == len(piramid[depth-1]):
                new_calculated_row.append(p2[depth-1][-1] + node)
            elif x == 0:
                new_calculated_row.append(p2[depth-1][0] + node)
        p2.append(new_calculated_row)
    # Get max value from last level
    print(max(plain_list(p2[-1])))


def sum_check_list(lst, n):
    '''
    Add n to each element in lst if lst is a list, else return
    a list with the sum of lst and n.
    '''
    if type(lst) == list:
        return [n+i for i in lst]
    return [lst+n]


def plain_list(l):
    '''
    Make l (list with ints and lists) a plain list, with all of his elems
    being int.
    '''
    pl = []
    for i in l:
        if type(i) == int:
            pl.append(i)
        else:
            pl.extend(i)
    return pl


@timer
def main():
    piramid = []
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pe_18_piramid.txt'), 'r') as f:
        for l in f.readlines():
            piramid.append(list(map(int, l.split())))
    maximum_path_sum(piramid)


if __name__ == "__main__":
    main()
