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


@challenge(name="Password Validation",
           level="Hard",
           desc="""
            Check if a password has at least 2 words and 2 special chars,
            and a minumum length of 7."""
           )
def password_validation():
    passw = input()
    print("Strong" if (re.match(r"^.*\d+.*\d+.*$", passw) and re.match(r"^.*[\!\@\#\$\%\&\*]+.*[\!\@\#\$\%\&\*]+.*$", passw) and len(passw) >= 7) else "Weak")


@challenge(name="Security",
           level="Hard",
           desc="""
            Evaluate a given floor of the casino to determine
            if there us a guard between the money and the thief,
            if there is not, you will sound an alarm."""
           )
def security():
    mapa = input().replace('x', '')
    money = mapa.index('$')
    print("quiet" if (money == 0 or mapa[money-1] != 'T') and (money == len(mapa)-1 or mapa[money+1] != 'T') else "ALARM")


@challenge(name="New Driver's License",
           level="Hard",
           desc="""
            Given everyone's name that showed up at the same
            time, determine how long it will take to get
            your new license."""
           )
def new_drivers_license():
    my_name = input()
    available_agents = int(input())
    others_names = input().split()
    others_names.append(my_name)
    print(sorted(others_names).index(my_name)//available_agents*20 + 20)

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
    def calcPi(limit):  # Generator function
        q, r, t, k, n, l = 1, 0, 1, 1, 3, 3
        decimal = limit
        counter = 0
        while counter != decimal + 1:
            if 4 * q + r - t < n * t:
                # yield digit
                yield n
                # insert period after first digit
                if counter == 0:
                        yield '.'
                # end
                if decimal == counter:
                        print('')
                        break
                counter += 1
                nr = 10 * (r - n * t)
                n = ((10 * (3 * q + r)) // t) - 10 * n
                q *= 10
                r = nr
            else:
                nr = (2 * q + r) * l
                nn = (q * (7 * k) + 2 + (r * l)) // (t * l)
                q *= k
                t *= l
                l += 2
                k += 1
                n = nn
                r = nr
    
    pi_digits = calcPi(int(input()))
    print([d for d in pi_digits][-1])
    

@challenge(name="Poker Hand",
           level="Hard",
           desc="""
            Output the rank of the give poker hand."""
           )
def poker_hand():
    class Card(object):
        def __init__(self, value, suite):
            self.value = int({"J":11,"Q":12,"K":13,"A":14}.get(value, value))
            self.suite = suite
        
        def __lt__(self, obj):
            return self.value < obj.value
        
    
    class PokerHand:
        def __init__(self):
            self.hand = []
            self.dict_values = {}
            self.dict_suites = {}
        
        def add_card(self, card):
            self.hand.append(card)
            self.dict_values[card.value] = self.dict_values.get(card.value, 0) + 1
            self.dict_suites[card.suite] = self.dict_suites.get(card.suite, 0) + 1

        def is_royal_flush(self):
            sorted_hand = sorted(self.hand)
            return sorted_hand[0].value == 10 and self.is_straight_flush()

        def is_straight_flush(self):
            return self.is_flush() and self.is_straight()

        def is_four_of_a_kind(self):
            return len([k for k,v in self.dict_values.items() if v == 4]) == 1

        def is_full_house(self):
            return self.is_three_of_a_kind() and self.is_one_pair()

        def is_flush(self):
            return len(set(self.dict_suites.keys())) == 1

        def is_straight(self):
            sorted_hand = sorted(self.hand)
            return sorted_hand[0].value + 4 == sorted_hand[-1].value

        def is_three_of_a_kind(self):
            return len([k for k,v in self.dict_values.items() if v == 3]) == 1

        def is_two_pairs(self):
            return len([k for k,v in self.dict_values.items() if v == 2]) == 2

        def is_one_pair(self):
            return len([k for k,v in self.dict_values.items() if v == 2]) == 1

        def get_rank(self):
            if self.is_royal_flush():
                return "Royal Flush"
            elif self.is_straight_flush():
                return "Straight Flush"
            elif self.is_four_of_a_kind():
                return "Four of a Kind"
            elif self.is_full_house():
                return "Full House"
            elif self.is_flush():
                return "Flush"
            elif self.is_straight():
                return "Straight"
            elif self.is_three_of_a_kind():
                return "Three of a Kind"
            elif self.is_two_pairs():
                return "Two Pairs"
            elif self.is_one_pair():
                return "One Pair"
            else:
                return "High Card"
    
    hand = PokerHand()
    str_hand = input().split()
    for c in str_hand:
        hand.add_card(Card(c[0:-1],c[-1]))
    print(hand.get_rank())

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
    perms = []
    for i in range(1, fact(len(word))):
        perms.append(nth_permutation(sorted(word), i))
    print(sorted(list(set(perms))).index(word)+1)



if __name__ == "__main__":
    (locals().get(sys.argv[1],lambda : print('No "{}" challenge found.\nAvailable challenges: {}'
        .format(sys.argv[1], [k for k,v in globals().items() if callable(v) and k != "challenge" ]))))()