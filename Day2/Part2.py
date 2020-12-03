import re
from itertools import accumulate

pattern = r'(\d+)-(\d+) (.): (.+)'
regex = re.compile(pattern)

def is_valid(s):
    m = regex.fullmatch(s)
    min = int(m.group(1))
    max = int(m.group(2))
    char = m.group(3)
    password = m.group(4)
    return (password[min-1] == char) ^ (password[max-1] == char)

with open("input.txt") as f:
    passwords = [l.strip() for l in f.readlines()]
    valid_count = sum(map(is_valid, passwords))
    print("Number of valid passwords: {0}".format(valid_count))