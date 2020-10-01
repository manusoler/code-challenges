import re
import math
from functools import reduce
from utils.decorators import challenge

# Challenges

@challenge(name="Popsicles", 
    level="Easy", 
    desc="""
        Given the number of siblings that you are giving pospsicles to, 
        determine if you can give them each an even amount or if you shouldn't 
        mention de pospsicles at all"""
)
def popsicles():
    sibligns = int(input())
    popsicles = int(input())
    print("give away" if popsicles % sibligns == 0 else "eat them yourlsef")

@challenge(name="Halloween Candy", 
    level="Easy", 
    desc="""
        Given the input of the total number of houses that you visited,
        what is the percentage change that one random item pulled from
        your bag is a dollar bill?"""
)
def halloween_candy():
    houses = int(input())
    print(math.ceil(2/houses*100))

@challenge(name="Fruit Bowl", 
    level="Easy", 
    desc="""
        Your task is to evaluate the total number of pies that you can make with 
        the apples that are in your bowl given to total amount of fruit in the bowl"""
)
def fruit_bowl():
    fruit = input()
    print(int(fruit/2/3))

@challenge(name="Ballpark Orders", 
    level="Easy", 
    desc="""
        Determine the total cost of ordering four items from the concession
        stand. If one of your friends orders something that isn't on the 
        menu, you will order a Coke for them instead"""
)
def ballpark_orders():
    order = input()
    prices = {'nachos':6,'pizza':6,'cheeseburger':10,'water':4,'coke':5}
    print(round(sum([prices.get(i.lower(),5) for i in order.split()])*1.07,2))

@challenge(name="Cheer creator", 
    level="Easy", 
    desc="""
        Given the number of yards that your team moved forward, output either
        "High Five" (for over 10), "shh" (for < 1), or a string that has a "Ra!"
        for every yard that they gained"""
)
def cheer_creator():
    yards = int(input())
    if yards > 10:
        print("High Five")
    elif yards < 1:
        print("shh")
    else:
        print("Ra!"*yards)

@challenge(name="Skee-Ball", 
    level="Easy", 
    desc="""
        Evaluate whether or not you have scored high enough
        to earn enough tickets to purchase
        the squirt gun at the arcade"""
)
def skee_ball():
    points = int(input())
    price = int(input())
    tickets = int(points/12)
    print("Buy it!" if tickets >= price else "Try again")

@challenge(name="Paint costs", 
    level="Easy", 
    desc="""
        Given the total number of color of paint that you need, calculate
        and output the total cost of  your project rounded up to the neartest 
        whole number"""
)
def paint_costs():
    colors_num = int(input())
    price = round((40+colors_num*5)*1.1,0)
    print(int(price))

@challenge(name="Argentina", 
    level="Easy", 
    desc="""
        Create a program that takes two prices and tells
        you which one is lower after conversion"""
)
def argentina():
    pesos = int(input())
    dollars = int(input())
    print("Pesos" if pesos*0.02 <= dollars else "Dollars")

@challenge(name="Balconies", 
    level="Easy", 
    desc="""
        Evaluate the area of two different balconies
        and determine which one is bigger"""
)
def balconies():
    lmb = lambda x,y: int(x)*int(y)
    a1 = reduce(lmb, input().split(','))
    a2 = reduce(lmb, input().split(','))
    print('Apartment A' if a1 >= a2 else 'Apartment B')

@challenge(name="Candles", 
    level="Easy", 
    desc="""
        Determine how many candles you need to order based
        on how many friends ask to join your order (each
        friend will nedd 9 candles)"""
)
def candles():
    print(int(input())*9+9)

@challenge(name="Duct Tape", 
    level="Easy", 
    desc="""
        Given the height and width  of the door, determine
        how many rolls of duct tape you will need (a roll
        is 60 feet long and 2 inches wide and there are 12 
        inches in each foot). Don't forget both sides of 
        the door"""
)
def duct_tape():
    door = int(input())*12 * int(input())*12 * 2
    tape = 60 * 12 * 2
    print(math.ceil(door/tape))

@challenge(name="Easter Eggs", 
    level="Easy", 
    desc="""
        If you know the total number of egss that were hidden and the 
        amount in both of your baket, evaluate where it is time
        to eat candy or keep hunting for more eggs"""
)
def easter_eggs():
    print('Keep Hunting' if int(input()) - (int(input()) + int(input())) > 0 else 'Candy Time')

@challenge(name="Guard Flamingos", 
    level="Easy", 
    desc="""
        Given the length and width of your rectangular yard, determine 
        how many flamingos you should buy to put one every 2 feet 
        along the edges of your yard"""
)
def guard_flamingos():
    print(int(input())+int(input()))

@challenge(name="Gotham City", 
    level="Easy", 
    desc="""
        Determine whether you need to call backup based on the total 
        number of criminals being reported"""
)
def gotham_city():
    villians = int(input())
    if villians < 5:
        print('I got this!')
    elif villians >= 5 and villians <= 10:
        print('Help me Batman')
    else:
        print('Good Luck out there!')

@challenge(name="Hovercraft", 
    level="Easy", 
    desc="""
        Determine whether or not you made a profit based on how many
        of the ten hovercrafts you were able to sell that month"""
)
def hovercraft():
    sells = int(input())
    spent = 21
    sellings = sells*3

    if spent < sellings:
        print('Profit')
    elif spent > sellings:
        print('Loss')
    else:
        print('Broke Even')

@challenge(name="Izzy the Iguana", 
    level="Easy", 
    desc="""
        Evaluate whether or not you have enough snack points to
        convince your iguana to come down"""
)
def izzy_the_iguana():
    d = {'Lettuce':5,'Carrot':4,'Mango':9}
    print('Come on Down!' if sum([d.get(s,0) for s in input().split()]) > 10 else 'Time to wait')

@challenge(name="Kaleidoscopes", 
    level="Easy", 
    desc="""
        Take the number of Kaleidoscopes that a customer buys
        and output their total cost including tax and any discounts"""
)
def kaleidoscopes():
    k = int(input())
    print(round(k*5*1.07*(0.9 if k > 1 else 1),2))

@challenge(name="Jungle Camping", 
    level="Easy", 
    desc="""
        You are given the noises made by different animals that you can hear
        in the dark, evaluate each noise to deterine which animal ir belongs
        to. Lions say Grr, Tigers say Rawr, Snakes say Ssss and Birds say Chirp"""
)
def jungle_camping():
    noises = input()
    noises_dict = {'Grr':'Lion', 'Rawr':'Tiger', 'Ssss':'Snake', 'Chirp':'Bird'}
    for i in noises.split():
        print(noises_dict[i], end='')

@challenge(name="Land Ho!", 
    level="Easy", 
    desc="""
        Determine your wait time if you know the total number of people ahead of you
        in line"""
)
def land_ho():
   print(int(input())//20*20+10)

@challenge(name="Neverland", 
    level="Easy", 
    desc="""
        Evaluate the difference between your ages and the age of your twin
        is now if you are given the age that you were when you got to
        Neverland, and the time has elapsed since then"""
)
def neverland():
    x = input()
    y = input()
    print('My twin is {} years old and they are {} years older than me'.format(x+y,y))




@challenge(name="Extra-Terrestrials", 
    level="Easy", 
    desc="""
        Take a word in english that you would like to say, and turn it
        into language that these aliens will understand"""
)
def extra_terrestrials():
    word = input()
    print(word[::-1])
    
@challenge(name="Zip Code Validator", 
    level="Easy", 
    desc="""
        Write a program that takes in a string representing
        a zip code. Output treo or false if it valid or not.
        A valid zip code is only numbers and 5 digits length"""
)
def zip_code_validator():
    print(str(re.match(r"^\d{5}$", input()) is not None))

@challenge(name="Vowel Counter", 
    level="Easy", 
    desc="""
        Write a program that takes in a string as input,
        counts and outputs the number of vowels"""
)
def vowel_counter():
    sent = input()
    print(sum([sent.lower().count(c) for c in "aeiou"]))
    
@challenge(name="Isogram Detector", 
    level="Easy", 
    desc="""
        Write a program that takes in a string as input,
        detects if the string is an isogram and outputs
        true or false based on the result"""
)
def isogram_detector():
    i = input()
    print(str(len(i) == len(set(i))).lower())

@challenge(name="Multiples", 
    level="Easy", 
    desc="""
        Given an integer number, output the sum of all
        the multipes of 3 and 5 below that number."""
)
def multiples():
    print(sum([i for i in range(int(input())) if i%3 == 0 or i%5 == 0]))

@challenge(name="Number of Ones", 
    level="Easy", 
    desc="""
        Count the number of ones in the binary representation
        of a given integer"""
)
def number_of_ones():
    print("{:b}".format(int(input())).count('1'))