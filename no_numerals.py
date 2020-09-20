# Take a phrase and replace any instances of an integer form 0-10 and replace it with the English word that corresponds to that integer
import re

if __name__ == '__main__':
    p = input()
    repl = {10:"ten", 0:"zero", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine"}

    for k,v in repl.items():
        p = re.sub("[\D]?("+str(k)+")[\D]", v, p)
    print(p)