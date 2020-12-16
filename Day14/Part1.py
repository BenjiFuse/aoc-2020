import re

mask_pattern = re.compile(r"mask = ((0|1|X)+)")
write_pattern = re.compile(r"mem\[(\d+)\] = (\d+)")

with open('input.txt') as f:
    lines = [l.strip() for l in f.readlines()]

    zero_mask = 0
    one_mask = 0
    mem = {}
    
    for l in lines:
        mgroups = mask_pattern.match(l)
        if mgroups:
            mask = mgroups[1]

            zero_mask = int(mask.replace('X', '1'),2)
            one_mask = int(mask.replace('X', '0'),2)
        else:
            wgroups = write_pattern.match(l)
            index = int(wgroups[1])
            value = int(wgroups[2])
            value = value & zero_mask
            value = value | one_mask

            mem[index] = value

    print(sum(list(mem.values())))
