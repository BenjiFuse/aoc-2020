import re
from typing import List

mask_pattern = re.compile(r"mask = ((0|1|X)+)")
write_pattern = re.compile(r"mem\[(\d+)\] = (\d+)")

def expand_with_mask(mask: str, value: int) -> List[int]:
    """returns all matching integers after applying the given mask to the value"""
    value_str = format(value, '036b')
    all_values = []

    if mask[0] == '0':
        all_values = [value_str[0]]
    elif mask[0] == '1':
        all_values = ['1']
    elif mask[0] == 'X':
        all_values = ['0', '1']

    for i, c in enumerate(mask[1:]):
        if c == '0':
            all_values = [v+value_str[i+1] for v in all_values]
        elif c == '1':
            all_values = [v+'1' for v in all_values]
        elif c == 'X':
            all_values = [v+n for n in ('0','1') for v in all_values]

    return [int(v,2) for v in all_values]

with open('input.txt') as f:
    lines = [l.strip() for l in f.readlines()]

    mask = ''
    mem = {}
    
    for l in lines:
        mgroups = mask_pattern.match(l)
        if mgroups:
            mask = mgroups[1]
        else:
            wgroups = write_pattern.match(l)
            index = int(wgroups[1])
            value = int(wgroups[2])

            indexes = expand_with_mask(mask, index)

            for i in indexes:
                mem[i] = value

    print(sum(list(mem.values())))
