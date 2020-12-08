import re

pattern_rule = re.compile(r'(.+)(?<!shiny gold) bags contain .+(shiny gold)')

with open('input.txt') as f:
    srules = f.read()
    conts = []
    matches = pattern_rule.findall(srules)
    while matches:
        for g in matches:
            g = matches.pop()
            conts.append(g[0])
            srules = srules.replace(g[0], g[1])
        matches = pattern_rule.findall(srules)

    print(len(set(conts)))
