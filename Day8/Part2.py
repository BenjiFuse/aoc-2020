import re

repl = {'nop':'jmp', 'jmp':'nop'}

def run(raw) -> int:
    lines = raw.split('\n')
    acc, ptr = 0, 0
    executed = []

    while ptr not in executed and ptr != len(lines)-1:
        executed.append(ptr)
        ins, val = lines[ptr].split()
        val = int(val)
        if ins == 'acc':
            acc += val
        elif ins == 'jmp':
            ptr += val
            continue
        ptr += 1
    
    return acc, ptr

with open('input.txt') as f:
    raw = f.read()    
    candidates = re.finditer(r'jmp|nop', raw)
    max_line = len(raw.split('\n'))-1
    for c in candidates:
        new_raw = raw[:c.start()] + repl[c.group()] + raw[c.end():]
        acc, ptr = run(new_raw)

        if ptr == max_line:
            print(acc)
            break