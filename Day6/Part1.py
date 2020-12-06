with open('input.txt') as f:
    groups = [g.replace('\n', '') for g in f.read().split('\n\n')]
    answers = [set(list(g)) for g in groups]
    print(sum([len(a) for a in answers]))