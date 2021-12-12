from fractions import Fraction
from functools import reduce

def product(fracs):
    t = # complete this line with a reduce statement
    return t.numerator, t.denominator
nume = []
deno = []
if __name__ == '__main__':
    for i in int(input()):
        nume.append(int(input()))
        deno.append(int(input()))
sum_num = reduce(lambda x,y : x+y,nume)
sum_deno = reduce(lambda x,y : x+y,deno)

print(Fraction(sum_num,sum_deno))