import re
import functools
from datetime import datetime
from utils.decorators import challenge

# Challenges

@challenge(name="It's a Sign",
           level="Hard",
           desc="""
            Given the four words that were supposed to be contained in each box,
            determine if at least one of them is of a palindrome."""
           )
def its_a_sign():
    words = [input() for i in range(4)]
    print("Open" if any([w == w[::-1] for w in words]) else "Trash")


@challenge(name="Mathematics",
           level="Hard",
           desc="""
            Test each math expression to find the first one that
            matches the answer that you are given"""
           )
def mathematics():
    result = int(input())
    oper = input()
    matchs = re.findall(r"\(((\d+[\+\-\*\/])+\d+)\) ?]", oper)
    results = [eval(m[0]) == result for m in matchs]
    print("none" if True not in results else "index {}".format(results.index(True)))


@challenge(name="2D Map",
           level="Hard",
           desc="""
            Determine the total number of moves that are needed between two points
            on a map. The points that you move between are marked with a P and the 
            spaces in between are marked with a X."""
           )
def map_2d():
    map2 = input().split(',')
    p1, p2 = None, None
    for x, arr in enumerate(map2):
        for y, elem in enumerate(arr):
            if elem == 'P':
                if not p1:
                    p1 = (x,y)
                else:
                    p2 = (x,y)
                    break
        if p1 and p2:
            break
    print(abs(p2[0]-p1[0]) + abs(p2[1]-p1[1]))


@challenge(name="Hofstadter's Q-Sequence",
           level="Hard",
           desc="""
            Given an intenger value input, determine and
            output the corresponding q-sequence value."""
           )
def hofstadters_q_sequence():
    def q(n):
        qarr = [1,1,2]
        for i in range(3,n):
            qarr.append(qarr[i-qarr[i-1]]+qarr[i-qarr[i-2]])
        return qarr[n-1]
    print(q(int(input())))


@challenge(name="Longest Common Substring",
           level="Hard",
           desc="""
            Given multiple words, you need to find the
            longest string that is a substring of all words."""
           )
def longest_common_substring():
    words = input().split()
    lcs = ""
    i, j = 0, 1
    while j <= len(words[0]):
        for w in words[1:]:
            if words[0][i:j] not in w:
                i += 1
                j = i+1
                break
        lcs = words[0][i:j] if len(lcs) < len(words[0][i:j]) else lcs
        j += 1
    print(lcs)


@challenge(name="Digits of Pi",
           level="Hard",
           desc="""
            Given an integer N as input, find and output the
            Nth decimal digit of Pi."""
           )
def digits_of_pi():
    pass


@challenge(name="Poker Hand",
           level="Hard",
           desc="""
            Output the rank of the give poker hand."""
           )
def poker_hand():
    pass


@challenge(name="Word rank",
           level="Hard",
           desc="""
            Given a word (not limited to just "dictionary
            words"), calculate and output its rank among 
            all the words that can be madre from the letters
            of that word. The word can contain duplicate
            letters."""
           )
def word_rank():
    fact = lambda x: functools.reduce(lambda i,j: i*j, range(1,x+1))

    def nth_permutation(elems, n):
        """
        Find nth lexicographic permutation of elems by calculating 
        the number of permutatios left for each position
        elems array with elements to permutate, must be sorted
        n the nth lexicographic permutation to find
        """
        pos, summ = 0, 0
        permutation = ""
        for i in reversed(range(1,len(elems))):
            fact_i = fact(i)
            while summ+fact_i < n:
                summ += fact_i
                pos += 1
            permutation += str(elems[pos])
            del(elems[pos])
            pos = 0
        return permutation + str(elems[0])
    
    word = input()
    for i in range(fact(len(word))):
        if nth_permutation(sorted(word), i) == word:
            print(i+1)
            break



if __name__ == "__main__":
    (locals().get(sys.argv[1],lambda : print('No "{}" challenge found.\nAvailable challenges: {}'
        .format(sys.argv[1], [k for k,v in globals().items() if callable(v) and k != "challenge" ]))))()