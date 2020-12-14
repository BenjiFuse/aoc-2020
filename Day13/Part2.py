def extended_euclidean(a, b):
    """Implementation of the extended euclidean algorithm for finding gcd
    and x,y to satisfy a*x + b*y == gcd"""
    if a == 0:
        return b, 0, 1
    
    gcd, x1, y1 = extended_euclidean(b%a, a)

    x = y1 - (b//a) * x1
    y = x1

    return gcd, x, y

def mod_inverse(a, m):
    g, x, y = extended_euclidean(a, m)
    return x % m

def crt(m, x):
    """Implementation of Chinese Remainder Theorem for combining modular equations"""
    while True:
        an = mod_inverse(m[1], m[0]) * x[0] * m[1] + \
                mod_inverse(m[0], m[1]) * x[1] * m[0]

        mn = m[0] * m[1]    # combine mod classes

        x = x[2:]           # remove first 2 remainders
        x = [an % mn] + x   # prepend combined remainder

        m = m[2:]           # remove first 2 mods
        m = [mn] + m        # prepend combined mod
    
        if len(x) == 1:     # final remainder found
            break
    
    return x[0], an, m      # returns final Xn, An, and Mn to satisy An = Xn mod(Mn)
    

with open('input.txt') as f:
    lines = f.read().split('\n')
    pairs = {int(n):i for i, n in enumerate(lines[1].split(',')) if n != 'x'}

    busses = list(pairs.keys())
    offsets = list(pairs.values())

    r, an, mn = crt(busses, offsets)
    print(mn[0] - r)    # subtract combined remainder from combined mod