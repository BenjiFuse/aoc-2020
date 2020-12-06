with open('input.txt', 'r') as f:
    lines = f.read().split()
    trans = str.maketrans('FBLR', '0101')
    passes = [int(line.translate(trans), 2) for line in lines]
    print(max(passes))