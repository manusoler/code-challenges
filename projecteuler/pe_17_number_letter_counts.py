import functools
from utils.decorators import timer
"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 
(one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""


def translate_number(n):
    trans_dict = { 1:"one", 2:"two", 3:"three", 4:"four", 5:"five",
              6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"ten",
              11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen",
              15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen",
              19:"nineteen", 20:"twenty", 30:"thirty", 40:"forty", 50:"fifty", 
              60:"sixty", 70:"seventy", 80:"eighty", 90:"ninety"}
    
    thousands, hundreds, tens, units = n // 1000, n % 1000 // 100, (n % 1000) % 100 // 10, n % 10
    translation = ""
    if thousands > 0:
        translation += " {} thousand".format(trans_dict[thousands])
    if hundreds > 0:
        translation += " {} hundred".format(trans_dict[hundreds])
    if tens > 0:
        if hundreds > 0 or thousands > 0:
            translation += " and"
        if tens > 1:
            translation += " {}".format(trans_dict[tens*10])
    if units > 0 or tens == 1:
        if tens > 1:
            translation += "-{}".format(trans_dict[units])
        else:
            if tens == 0 and (hundreds > 0 or thousands > 0):
                translation += " and"
            translation += " {}".format(trans_dict[tens*10+units])
    #print("{} -> {}".format(n, translation.lstrip()))
    return translation.lstrip()


def number_letter_counts(n):
    return len(translate_number(n).replace(" ", "").replace("-",""))


@timer
def main():
    summ, n = 0, 1000
    for i in range(1,n+1):
        summ += number_letter_counts(i)
    print("Total letter counts from 1 to {}: {}".format(n, summ))

if __name__ == "__main__":
    main()