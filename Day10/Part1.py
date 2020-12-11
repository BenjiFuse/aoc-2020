with open('input.txt') as f:
    adapters = [int(i) for i in f.readlines()]

    adapters.extend([0, max(adapters) + 3])
    adapters.sort()

    diffs = {1:0, 2:0, 3:0}
    for i in range(0, len(adapters)-1):
        d = adapters[i+1] - adapters[i]
        diffs[d] = diffs[d]+1

    print(diffs[1]*diffs[3])