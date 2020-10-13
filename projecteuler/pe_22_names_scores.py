import requests
from utils.decorators import timer
"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

def names_scores(names):
    names.sort()
    abcd = "abcdefghijklmnopqrstuvwxyz"
    return [sum([abcd.index(l)+1 for l in n])*(i+1) for i, n in enumerate(names)]
    

@timer
def main():
    r = requests.get('https://projecteuler.net/project/resources/p022_names.txt', verify=False)
    names = [n.replace('"','').lower() for n in r.text.split(",")]
    print(sum(names_scores(names)))

if __name__ == "__main__":
    main()