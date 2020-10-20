from utils.decorators import timer
"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
-----
Si hacemos la espiral 7x7, apreciamos varias cosas:
1. Las matrices de espirales van creciendo de 2 en 2; 1, 3, 5, 7, ...
2. El mayor numero de la diagonal es el cuadrado de la matriz, e.d. en la 1x1 es el 1, en la 3x3 es el 9, en la 5x5 es el 25 y en la 7x7 es el 49

Por tanto las diagonales para cada matriz las podemos calcular con la formula: n**2 - (n-1)*d, donde n es el tamaño de la matriz, y d va de 0 a 3 (las 4 esquinas).

Así que para la matriz 1001x1001 solo hay que iterar desde 1 hasta 1001 (de 2 en 2) y aplicar esta formula en cada iteracion.
"""

def number_spiral_diagonals(n):
    """
    Get the 4 numbers in the diagonals of a number spiral n*n 
    """
    if n == 1:
        return [1]
    return [n**2 - (n-1)*d for d in range(0,4)]


def sum_number_spiral_diagonals(n):
    summ = 0
    for i in range(1,n+1,2):
        #print(i, number_spiral_diagonals(i))
        summ += sum(number_spiral_diagonals(i))
    return summ


@timer
def main():
    print(sum_number_spiral_diagonals(1001))


if __name__ == "__main__":
    main()
