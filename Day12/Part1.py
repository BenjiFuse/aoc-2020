from numpy import array as a

dirmap = {'N':[-1,0], 'E':[0,1], 'S':[1,0], 'W':[0,-1]}
dir_vecs = list(dirmap.values())
turnmap = {'L':-1, 'R':1}


with open('input.txt') as f:
    moves = [(l[0], int(l[1:])) for l in f.readlines()]

    position = a([0,0])
    direction = dirmap['E']

    for m in moves:
        if m[0] in dirmap.keys():
            position += m[1] * a(dirmap[m[0]])
        elif m[0] in ('L', 'R'):
            turns = (m[1] // 90) * turnmap[m[0]]
            i = dir_vecs.index(direction)
            i = (i+turns) % 4
            direction = dir_vecs[i]
        elif m[0] == 'F':
            position += m[1] * a(direction)

    print("Manhattan distance: %d" % sum(abs(position)))