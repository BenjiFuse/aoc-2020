import re

range_pattern = re.compile(r'(.+): (\d+)-(\d+) or (\d+)-(\d+)')
NEARBY_HEADER = 'nearby tickets:'

def range_factory(a,b,c,d):
    return lambda x: (a <= x <= b) or (c <= x <= d)

with open('input.txt') as f:
    raw = f.read()

    range_grps = range_pattern.findall(raw)
    
    nearby_tickets = [i.split(',') for i in raw[raw.find(NEARBY_HEADER):].split('\n')][1:-1]
    nearby_tickets = [[int(i) for i in line] for line in nearby_tickets]
    
    conditions = {}
    for grp in range_grps:
        a,b,c,d = [int(i) for i in grp[1:]]
        conditions[grp[0]] = range_factory(a,b,c,d)

    invalids = []
    for t in nearby_tickets:
        for i in t:
            has_match = False
            for field, cond in conditions.items():
                has_match = cond(i)
                if has_match: break
            if not has_match:
                invalids.append(i)
    
    print(sum(invalids))