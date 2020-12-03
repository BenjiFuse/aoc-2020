with open('input.txt') as f:
    lines = [l.strip() for l in f.readlines()]
    x = 0
    hits = 0
    for line in lines[1:]:
        x = (x + 3) % 31
        if line[x] == '#':
            hits += 1

    print("Total hits: {0}".format(hits))