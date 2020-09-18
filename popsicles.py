# Given the number of siblings that you are giving pospsicles to, 
# determine if you can give them each an even amount or if you shouldn't 
# mention de pospsicles at all

sibligns = int(input())
popsicles = int(input())

print("give away" if popsicles % sibligns == 0 else "eat them yourlsef")