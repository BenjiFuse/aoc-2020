acc = 0
ptr = 0
executed = []

with open('input.txt') as f:
    lines = f.readlines()

    while ptr not in executed:
        executed.append(ptr)
        ins, val = lines[ptr].split()
        val = int(val)
        if ins == 'acc':
            acc += val
        elif ins == 'jmp':
            ptr += val
            continue
        ptr += 1
        
    print(acc)
        
