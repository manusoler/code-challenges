import re
import sys
import math
import string
from datetime import datetime

# Decorator
def challenge(*args, **kwargs):
    def inner(func):
        def wrapper(*args1, **kwargs1):
            print("Running challenge...\nName: {} ({})\nDescription:{}".format(kwargs["name"],kwargs["level"],kwargs["desc"]))
            func(*args1, **kwargs1)
        return wrapper
    return inner


# Challenges
@challenge(name="Pig Latin", 
    level="Medium", 
    desc="""
        Take a sentence in English and turn it into the same sentence in Pig Latin!"""
)
def pig_latin():
    sentence = input()
    words = sentence.split()
    transl = ""
    for w in words:
        transl += w[1:] + w[0] + "ay "

    print(transl[:-1])

@challenge(name="Military Time", 
    level="Medium", 
    desc="""
        Determine if the time you are given is AM or PM, then convert that value 
        to the way that if would apper on a 24 hour clock"""
)
def military_time():
    time = input('')
    pattern = r"^([01]?[0-9]):([0-5][0-9]) (AM|PM)$"

    match = re.search(pattern, time)
    if match:
        hour = int(match.group(1))
        minutes = match.group(2)
        m = match.group(3)

        if m == "PM":
            hour = (hour + 12) % 24
        
        print("{:02d}:{}".format(hour, minutes))
    else:
        print("Incorrect time format, must be: HH:MM (AM|PM)")

@challenge(name="That's odd...", 
    level="Medium", 
    desc="""
        Find the sum of all even integers in a list of numbers"""
)
def thats_odd():
    size = int(input())
    sum = 0
    for i in range(size):
        num = int(input())
        sum += num if num % 2 == 0 else 0
    print(sum)

@challenge(name="Average Word Length", 
    level="Medium", 
    desc="""
        Takes in a string, figure out the average length of all the
        words and return a number representing the average length.
        Remove all punctuacion. Round up to the nearest whole number"""
)
def average_word_length():
    essay = input()
    re.sub(r"\.,","",essay)
    words_num = len(essay.split())
    word_len = len(re.findall(r"[a-zA-Z]", essay))
    print(math.ceil(word_len/words_num))

@challenge(name="No numerals", 
    level="Medium", 
    desc="""
        Take a phrase and replace any instances of an integer 
        form 0-10 and replace it with the English word that 
        corresponds to that integer"""
)
def no_numerals():
    p = input()
    repl = {10:"ten", 0:"zero", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine"}
    for k,v in repl.items():
        p = re.sub(r"\b("+str(k)+r")\b", v, p)
    print(p)

@challenge(name="Youtube link finder", 
    level="Medium", 
    desc="""
        Create a program that parses through a link, extracts
        and outputs the YouTube video ID"""
)
def youtube_link_finder():
    url = input()
    id = url.split('/')[-1]
    print(id if not id.startswith("watch") else id.split('=')[-1])

@challenge(name="Secret Message", 
    level="Medium", 
    desc="""
        Create a program that replaces each letter in a message
        with its corresponding letter in a backwars version of 
        the English alphabet"""
)
def secret_message():
    alpha = string.ascii_lowercase
    alp_rev = string.ascii_lowercase[::-1]
    phrase = input().lower()
    print("".join((alp_rev[alpha.index(i)] if i in alpha else i) for i in phrase))

@challenge(name="Symbols", 
    level="Medium", 
    desc="""
        Take a text that includes some random symbols and translate it 
        into a text that has none of them. The resulting text should only
        include letters and numbers"""
)
def symbols():
    print(re.sub(r"[^0-9a-zA-Z ]","",input()))

@challenge(name="The Spy Life", 
    level="Medium", 
    desc="""
        Create a program that will take the encoded message, flip it 
        around, remove any characters that are not a letter or a space
        , and output the hidden message"""
)
def the_spy_life():
    msg = input()
    print("".join(re.findall(r"[A-Za-z ]",msg)[::-1]))

@challenge(name="Deja Vu", 
    level="Medium", 
    desc="""
        If you are gicen a string of random letters, your task is to
        evaluate thether any letter is repeated in the string or if 
        you only hit unique keys while you typing"""
)
def deja_vu():
    string = input()
    dv = False
    for i in string:
        if string.count(i) > 1:
            dv = True
            break
    print("Deja Vu" if dv else "Unique")

@challenge(name="Converts US date to EU date", 
    level="Medium", 
    desc="""
        Create a function that takes in a string containung a date
        that is in US format, and retur a string of the same date
        converted to EU"""
)
def us_date_to_eu():
    us_date = input()
    fmat = r'%B %d,%Y'
    if re.match(r'\d{1,2}/\d{1,2}/\d{4}', us_date):
        fmat = r'%m/%d/%Y'
    time = datetime.strptime(us_date,fmat)
    print(re.sub(r"\b(0)\B","",time.strftime(r'%d/%m/%Y')))

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
    print("Pesos" if pesos*0.02 <= dollar else "Dollars")

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
    
@challenge(name="Extra-Terrestrials", 
    level="Easy", 
    desc="""
        Take a word in english that you would like to say, and turn it
        into language that these aliens will understand"""
)
def extra_terrestrials():
    word = input()
    print(word[::-1])

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
        prtin('Broke Even')

if __name__ == "__main__":
    (locals().get(sys.argv[1],lambda : print('No "{}" challenge found.\nAvailable challenges: {}'
        .format(sys.argv[1], [k for k,v in globals().items() if callable(v) and k != "challenge" ]))))()