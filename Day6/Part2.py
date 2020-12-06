with open('input.txt') as f:
    groups = [g.split() for g in f.read().split('\n\n')]

    total = 0
    for group in groups:
        max = len(group)
        all = [item for person in group for item in person]
        ans = set(all)
        for a in ans:
            total += all.count(a) == max

    print(total)
