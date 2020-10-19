import re
from utils.decorators import timer
"""
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""

def get_decimals(dividendo,divisor,precission):
    resto = dividendo % divisor
    if resto:
        decimals = ""
        while len(decimals) < precission and resto:
            dividendo = resto * 10
            cociente = dividendo // divisor
            decimals += str(cociente)
            resto = dividendo % divisor
        return decimals
    return "0"


@timer
def main():
    pattern = r"\d{3}(\d+?)\1\d*"
    maxx, val = 0, 0
    for d in range(1,1000):
        dec = get_decimals(1,d,3000)
        f = re.findall(pattern, dec)
        if f and len(f) > 0 and len(f[0]) > maxx:
            maxx = len(f[0])
            val = d
    print(val, maxx)


if __name__ == "__main__":
    main()
