import re
from math import prod

range_pattern = re.compile(r'(.+): (\d+)-(\d+) or (\d+)-(\d+)')

your_ticket_pattern = re.compile('your ticket:\n(.+)\n')
nearby_tickets_pattern = re.compile('nearby tickets:\n((.|\n)+)')

def range_factory(a,b,c,d):
    """Wrapper to ensure condition range values remain in scope at evaluation"""
    return lambda x: (a <= x <= b) or (c <= x <= d)

def get_invalids(tickets, conditions):
    """Returns a list of every invalid ticket (list of ints) in tickets.
    Invalid tickets fail one or more of the provided conditions"""
    invalids = []
    for t in tickets:
        for i in t:
            has_match = False
            for field, cond in conditions.items():
                has_match = cond(i)
                if has_match: break
            if not has_match:
                invalids.append(t)
                break
    return invalids

def remove_from_values(d:dict, v):
    for field, indexes in d.items():
        indexes.remove(index)

with open('input.txt') as f:
    # parse inputs:
    raw = f.read()
    range_grps = range_pattern.findall(raw)
    nearby_ticket_lines = nearby_tickets_pattern.search(raw)[1].strip().split('\n')
    nearby_tickets = [[int(i) for i in line.split(',')] for line in nearby_ticket_lines]
    your_ticket = [int(i) for i in your_ticket_pattern.search(raw)[1].split(',')]

    # build field range condition dict {'field name'->range_condition(x)}:
    conditions = {}
    for grp in range_grps:
        a,b,c,d = [int(i) for i in grp[1:]]
        conditions[grp[0]] = range_factory(a,b,c,d)

    # remove all invalid tickets:
    for t in get_invalids(nearby_tickets, conditions):
        nearby_tickets.remove(t)

    # build lists of value indexes that satisfies each rule:
    field_to_valid_indexes = {c:[] for c,_ in conditions.items()}
    for field, cond in conditions.items():
        for i in range(len(nearby_tickets[0])):
            all_match = True
            for t in nearby_tickets:
                match = cond(t[i])
                if not match:
                    all_match = False
                    break
            if all_match:
                field_to_valid_indexes[field] = field_to_valid_indexes[field] + [i]
                continue

    # map each field to its respective index:
    fields = list(conditions.keys())
    field_to_index = {c:-1 for c,_ in conditions.items()}
    while (-1) in field_to_index.values():
        for field in fields:
            indexes = field_to_valid_indexes[field]
            if len(indexes) == 1:
                index = field_to_valid_indexes.pop(field)[0]  # remove field from candidates dict
                fields.remove(field)                          # remove from fields to match
                field_to_index[field] = index                 # match field to index
                remove_from_values(field_to_valid_indexes, index) # remove index as a candidate other fields

    # multiply all 'departure' fields values
    departure_indexes = list(field_to_index.values())[:6]
    print(prod([your_ticket[i] for i in departure_indexes]))