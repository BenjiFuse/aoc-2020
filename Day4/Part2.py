import re
from ast import literal_eval

required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

pattern_height = re.compile(r'^(\d+)(in|cm)$')
pattern_haircolor = re.compile(r'^#[a-f0-9]{6}$')
pattern_eyecolor = re.compile(r'^(amb|blu|brn|gry|grn|hzl|oth)$')
pattern_pid = re.compile(r'^\d{9}$')

with open('input.txt') as f:
    # Do a lil stringy dance so we can eval the inputs as dicts:
    a = f.read().strip()
    a = "{'" + a.replace("\n\n", "'},{'") + "'}"
    a = a.replace("\n", " ")
    a = a.replace(" ", "','")
    a = a.replace(":", "':'")
    
    passports = literal_eval(a)
    valids = 0

    for pp in passports:
        # early exit for missing fields
        if not all(field in pp for field in required):
            continue
        
        # validate all year properties
        if not (1920 <= int(pp['byr']) <= 2002): continue
        if not (2010 <= int(pp['iyr']) <= 2020): continue
        if not (2020 <= int(pp['eyr']) <= 2030): continue
        
        # validate height property
        try:
            match = pattern_height.fullmatch(pp['hgt'])
            height = int(match.group(1))
            unit = match.group(2)
            if unit == 'cm':
                if not (150 <= height <= 193):
                    continue
            elif unit == 'in':
                if not (59 <= height <= 76):
                    continue
        except:
            continue

        # validate remaining pattern-based properties
        if not pattern_haircolor.fullmatch(pp['hcl']): continue
        if not pattern_eyecolor.fullmatch(pp['ecl']): continue
        if not pattern_pid.fullmatch(pp['pid']): continue
            
        valids += 1
    
    print(valids)