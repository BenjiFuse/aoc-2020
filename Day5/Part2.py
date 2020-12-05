with open('input.txt') as f:
    lines = f.read().split()
    trans = str.maketrans('FBLR', '0101')
    passes = [int(line.translate(trans), 2) for line in lines]

    all_passes = range(min(passes), max(passes))
    missing_passes = set(all_passes) - set(passes)
    print(missing_passes)