import numpy as np
import matplotlib.pyplot as plt
from  matplotlib.animation import FuncAnimation


def count_seen_occupied_seats(m, i, j):
    deltas = [(r, c) for r in (-1,0,1) for c in (-1,0,1)]
    deltas.remove((0,0))
    
    counts = 0
    for d in deltas:
        r = i+d[0]
        c = j+d[1]

        while(0 <= r < m.shape[0] and 0 <= c < m.shape[1]):
            e = m[r,c]
            if e == 0:     
                break      # saw unoccupied seat in direction d
            elif e == 1:
                counts += 1 # saw occupied seat in direction d
                break
            r,c = r+d[0], c+d[1] # go forward in direction d

    return counts

def get_seen_matrix(m):
    rows,cols = m.shape
    s = np.empty_like(m)

    for r in range(rows):
        for c in range(cols):
            s[r,c] = -1 if m[r,c] == -1 else count_seen_occupied_seats(m, r, c)
                        
    return s

def iterate_seats(m, is_floor):

    seen = get_seen_matrix(m)
    
    now_occupied = (m == 0) & (seen == 0)
    now_vacant = (m == 1) & (seen >= 5)

    temp = m
    temp = np.where(now_occupied, 1, temp)
    temp = np.where(now_vacant, 0, temp)
    temp = np.where(is_floor, -1, temp)
    
    return temp

def get_floor_map(m):
    """returns a boolean np array corresponding to where the floor is"""
    am = m < 0
    return am

def animate_soln(frames):
    fig = plt.figure()
    plot = plt.imshow(frames[0], vmin=-1, vmax=1)

    def init():
        return update(0)

    def update(j):
        plot.set_data(frames[j])
        return [plot]

    anim = FuncAnimation(fig, update, init_func=init, frames=len(frames), interval=300, blit=False, repeat=False)
    plt.show()

with open('input.txt') as f:
    char_map = {'.':-1, 'L':0, '#':1}
    m = [l.strip() for l in f.readlines()]
    m = np.array([[char_map[c] for c in l] for l in m])
    is_floor = get_floor_map(m)

    frames = [m, iterate_seats(m, is_floor)]
    i = 1
    while not np.array_equal(frames[i-1], frames[i]):
        next = iterate_seats(frames[i], is_floor)
        frames.append(next)
        i += 1

    print("Occupied seats: %d" % np.sum(frames[-1] > 0))

    animate_soln(frames)