from math import gcd
from functools import reduce

def lcm(l):
    return reduce(lambda a,b: a*b // gcd(a,b), l)

def is_proper_offset(times):
    return

def find_index_where_offset(a, b, offset):
    

with open('input.txt') as f:
    lines = f.read().split('\n')
    busses = {int(n):i for i, n in enumerate(lines[1].split(',')) if n != 'x'}

    time = lcm(busses.keys())
    r_busses = list(busses.items()).reverse()

    i = 1
    while not is_proper_offset(time):
        r = 
        i += 1

    print(busses, l)