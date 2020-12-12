from numpy import array as a

dirmap = {'N':[-1,0], 'E':[0,1], 'S':[1,0], 'W':[0,-1]}
turnmap = {'L':-1, 'R':1}

def rotate(p, deg):
    """rotate origin around position by degrees"""
    turns = abs(deg // 90)

    for turn in range(turns):
        if deg > 0: #clockwise
            p = a([p[1], -p[0]])
        if deg < 0: #counter-clockwise
            p = a([-p[1], p[0]])
    
    return p

with open('input.txt') as f:
    moves = [(l[0], int(l[1:])) for l in f.readlines()]

    ship_position = a([0,0])
    waypoint_position = a([-1,10])  # relative to ship

    for m in moves:
        # translate waypoint in compass dir:
        if m[0] in dirmap.keys():
            waypoint_position += m[1] * a(dirmap[m[0]])
        # rotate waypoint about ship:
        elif m[0] in ('L', 'R'):
            deg  =  turnmap[m[0]] * m[1]
            waypoint_position = rotate(waypoint_position, deg)
        # advance ship towards waypoint:
        elif m[0] == 'F':
            ship_position += m[1] * waypoint_position

    print(ship_position)
    print("Manhattan distance: %d" % sum(abs(ship_position)))