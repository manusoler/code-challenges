import re
import sys
import math
import string
from datetime import datetime
from utils.decorators import challenge

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

@challenge(name="Roadrunner", 
    level="Medium", 
    desc="""
        Determine wheter or not the roadrunner made it to safety."""
)
def roadrunner():
    distance = int(input())
    roadrunner_speed = int(input())
    coyote_speed = int(input())
    print("Meep Meep" if (50+distance)/coyote_speed > distance/roadrunner_speed else "Yum")

@challenge(name="Super Sale", 
    level="Medium", 
    desc="""
        Given the prices of items you want to purchase, 
        determine how much you will save during your shoppings!"""
)
def super_sale():
    prices = [float(i) for i in input().split(",")]
    prices.sort(reverse=True)
    prices.pop(0)
    saved = 0
    for p in prices:
        saved += p*0.3
    saved *= 1.07
    print(int(saved))

@challenge(name="Carrot Cake", 
    level="Medium", 
    desc="""
        Determine if you will have enough leftover carrots to make your cake"""
)
def carrot_cake():
    carrots = int(input())
    boxes = int(input())
    print("Cake Time" if carrots % boxes >= 7 else "I need to buy {} more".format(7 - carrots % boxes))

@challenge(name="Building Blocks", 
    level="Medium", 
    desc="""
        If you know how may of each color block you have, 
        add up the leftover blocks to come up with the
        amount you will have after you have evenly 
        distributed each color to all 15 studentes"""
)
def building_blocks():
    blocks = [int(input()) for x in range(4)]
    leftovers = sum([b%15 for b in blocks])
    print(leftovers)

@challenge(name="Name Budy", 
    level="Medium", 
    desc="""
        Determine if anyone in your group has the same first
        letter of their name as you."""
)
def name_buddy():
    names = input().split()
    my_name = input()
    print("Compare notes" if any([my_name[0] == s[0] for s in names]) else "No such luck")

@challenge(name="Divisible", 
    level="Medium", 
    desc="""
        Test your number against all of the other numbers that
        you are given to make sure that it is divisble by them"""
)
def divisible():
    my_int = int(input())
    ints = [int(x) for x in input().split()]
    print("divisible by all" if all([my_int % i == 0 for i in ints]) else "not divisible by all")

@challenge(name="Even Numbers", 
    level="Medium", 
    desc="""
        Evaluate each number in your list to see if it is even or odd.
        Then, output a new list that only contains the even
        numbers from your original list."""
)
def even_numbers():
    print(" ".join([x for x in input().split() if int(x) % 2 == 0]))

@challenge(name="Tax Free", 
    level="Medium", 
    desc="""
        Determine the total cost once you include tax of 7%
        on the items that are still taxed."""
)
def tax_free():
    prices = [float(x) if float(x) > 20 else float(x)*1.07 for x in input().split(',')]
    print(round(sum(prices),2))

@challenge(name="How Far?", 
    level="Medium", 
    desc="""
        Evaluate how many blocks you'll have to walk if you
        are given a representation of your street where H 
        represents the pond, and every B representas a block 
        in between the two."""
)
def how_far():
    m = re.match(r"^.*[HP](B*)[HP].*$", input())
    print(len(m.group(1)))

@challenge(name="Day of the Week", 
    level="Medium", 
    desc="""
        Create a program that intakes in a string containing
        a date, and outputs the day of the week."""
)
def day_of_the_week():
    print(datetime.strptime(input(),'%m/%d/%Y').strftime('%A'))

@challenge(name="Camel to Snake", 
    level="Medium", 
    desc="""
        Write a program that takes in a string that has camel casing,
        and outputs the same string but with snake casing."""
)
def camel_to_snake():
    txt = input()
    print(txt[0].lower() + re.sub(r"([A-Z])","_\g<1>",txt[1:]).lower())

@challenge(name="Days between dates", 
    level="Medium", 
    desc="""
        Calculate how many days have passed between two input dates
        and output the result"""
)
def days_between_dates():
    dt1 = datetime.strptime(input(), '%B %d, %Y')
    dt2 = datetime.strptime(input(), '%B %d, %Y')
    print((dt2-dt1).days)

@challenge(name="Snowballing Numbers", 
    level="Medium", 
    desc="""
        Create a program that takes in an array of
        numbers, check if each number is greater than
        the sum of all previous numbers, and output
        true if the condition is met, and false, if not."""
)
def snowballing_numbers():
    n = int(input())
    summ, cond = 0, True
    for i in range(n):
        a = int(input())
        if a <= summ:
            cond = False
        summ += a
    print(str(cond).lower())

@challenge(name="Flowing Words", 
    level="Medium", 
    desc="""
        Write a program that takes in a string that
        contains a sentence, checks if the first letter of
        each word is the same as the last letter of the
        previous one. If the condition es met, output
        true, if not false.
        Casing does not matter."""
)
def flowing_words():
    print("false" if re.match(r"(\w) (?!\1)", input()) else "true")

@challenge(name="Missing Numbers", 
    level="Medium", 
    desc="""
        """
)
def missing_numbers():
    pass

@challenge(name="Initials", 
    level="Medium", 
    desc="""
        """
)
def initials():
    pass

@challenge(name="Credit Card Validator", 
    level="Medium", 
    desc="""
        """
)
def creadit_card_validator():
    pass

@challenge(name="CMYK to RGB", 
    level="Medium", 
    desc="""
        """
)
def cmyk_to_rgb():
    pass


@challenge(name="Safety Deposit Boxes", 
    level="Medium", 
    desc="""
        Determine the amount of time it will take you to
        find the item you are looking for if it takes
        you 5 minutes to drill into each box"""
)
def safety_deposit_boxes():
    stuff = input().split(',')
    obj = input()
    print((stuff.index(obj)+1)*5)

@challenge(name="Snap, Crackle and Pop", 
    level="Medium", 
    desc="""
        Based on the quentities in each bowl, output the noise
        that they make"""
)
def snap_crackle_pop():
    bowl = []
    for i in range(6):
        bowl.append(int(input()))
    f = lambda x: "Pop" if not x%3 else ("Snap" if not x%2 else "Crackle")
    print(" ".join([f(s) for s in bowl]))

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

@challenge(name="Hex Color Code Generator", 
    level="Medium", 
    desc="""
        Create a function that accepts three integers that represent
        the RGB values an outpurs the hex-code representation."""
)
def hex_color_code_generator():
    print("#{:x}{:x}{:x}".format(int(input()), int(input()), int(input())))

@challenge(name="Symbols", 
    level="Medium", 
    desc="""
        Take a text that includes some random symbols and translate it 
        into a text that has none of them. The resulting text should only
        include letters and numbers"""
)
def symbols():
    print(re.sub(r"[^0-9a-zA-Z ]","",input()))

@challenge(name="Duty Free", 
    level="Medium", 
    desc="""
        Evaluate each item that you purchased to make sure that 
        didn't spend more than $20 on that particular item. 
        If you did, you will need to go back to the store to 
        return it"""
)
def duty_free():
    print('Back to the store' if any([float(x)*1.1 > 20 for x in input().split()]) else 'On to the terminal')

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

@challenge(name="Text Decompressor", 
    level="Medium", 
    desc="""
        Write a program that takes the compressed text as 
        input and outputs the decompressed version."""
)
def text_decompressor():
    text = input()
    chars = zip(text[::2],text[1::2])
    print("".join([c[0]*int(c[1]) for c in chars]))

@challenge(name="Splitting Strings", 
    level="Medium", 
    desc="""
        Write a program that takes in a string, and a number as input.
        Split the string into even parts sized by the number, 
        and output the parts separated by hyphens.
        The last part of the output will be any leftover, as the input
        string might not split into the provided parts evenly."""
)
def splitting_strings():
    text = input()
    parts = int(input())
    print("-".join([text[i:i+parts] for i in range(0,len(text), parts)]))

if __name__ == "__main__":
    (locals().get(sys.argv[1],lambda : print('No "{}" challenge found.\nAvailable challenges: {}'
        .format(sys.argv[1], [k for k,v in globals().items() if callable(v) and k != "challenge" ]))))()