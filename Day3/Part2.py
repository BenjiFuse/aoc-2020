with open('input.txt') as f:
    lines = [l.strip() for l in f.readlines()]
    x1_1, x1_3, x1_5, x1_7, x2_1 = 0,0,0,0,0
    hits1_1, hits1_3, hits1_5, hits1_7, hits2_1 = 0,0,0,0,0

    for i, line in enumerate(lines[1:]):
        # process m=2 movement and collisions:
        if i % 2 == 1:
            x2_1 = (x2_1 + 1) % 31
            if line[x2_1] == '#':
                hits2_1 += 1
                
        #process m=1 movements:
        x1_1 = (x1_1 + 1) % 31
        x1_3 = (x1_3 + 3) % 31
        x1_5 = (x1_5 + 5) % 31
        x1_7 = (x1_7 + 7) % 31

        # check m=1 collisions:
        if line[x1_1] == '#':
            hits1_1 += 1
        if line[x1_3] == '#':
            hits1_3 += 1
        if line[x1_5] == '#':
            hits1_5 += 1
        if line[x1_7] == '#':
            hits1_7 += 1

    print("hits in order: {0}, {1}, {2}, {3}, {4}".format(hits1_1, hits1_3, hits1_5, hits1_7, hits2_1))
    print("Product of all hits: {0}".format(hits1_1 * hits1_3 * hits1_5 * hits1_7 * hits2_1))