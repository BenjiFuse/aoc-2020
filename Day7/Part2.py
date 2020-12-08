import re

pattern_outer = re.compile(r'(.+) bags contain')
pattern_inner = re.compile(r'(\d+) (\w+ \w+) bags?')

class Bag():
    
    def __init__(self, color, quantity):
        self.color = color
        self.quantity = quantity
        self.content = []

def recurse_rules(color, qty):
    s = raw.find('%s bags contain' % color)
    e = raw.find('.', s)
    sub = raw[s:e+1]

    matches = pattern_inner.findall(sub)

    bag = Bag(color, int(qty))
    content = []
    for m in matches:
        content.append(recurse_rules(m[1], m[0]))
    bag.content = content

    return bag

def count_bags(bag):
    count = 0
    if bag.content == []:
        count = bag.quantity
    else:
        count += bag.quantity
        for b in bag.content:
            count += bag.quantity * count_bags(b)
    return count
    

with open('input.txt') as f:
    raw = f.read()
    shiny = recurse_rules('shiny gold', 1)
    print(count_bags(shiny)-1)