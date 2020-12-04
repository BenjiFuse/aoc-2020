required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

with open('input.txt') as f:
    a = f.read()
    a = a.replace('\n\n', '|')
    a = a.replace('\n', ' ')
    lines = a.split('|')
    
    valids = 0
    for line in lines:
        valid = all(field in line for field in required)
        valids += valid

    print(valids)