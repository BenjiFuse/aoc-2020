import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import convolve
from matplotlib.animation import FuncAnimation

k = np.array([[1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]])


def iterate_seats(m, am):
    adj = convolve(m, k, mode='constant', cval=0)
    
    now_occupied = (m == 0) & (adj == 0)
    now_vacant = (m == 1) & (adj >= 4)

    temp = m
    temp = np.where(now_occupied, 1, temp)
    temp = np.where(now_vacant, 0, temp)
    temp = np.where(am, 0, temp) # replace (-1) floor tiles with (0) so they don't effect adjacency
    
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
        """When rendering, swap in (-1) for the value of any floor tiles"""
        temp = np.where(is_floor, -1, frames[j])
        plot.set_data(temp)
        return [plot]

    anim = FuncAnimation(fig, update, init_func=init, frames=len(frames), interval=500, blit=False, repeat=False)
    plt.show()

with open('input.txt') as f:
    char_map = {'.':-1, 'L':0, '#':1}
    m = [l.strip() for l in f.readlines()]
    m = np.array([[char_map[c] for c in l] for l in m])
    is_floor = get_floor_map(m)

    m[m < 0] = 0
    frames = [m, iterate_seats(m, is_floor)]
    i = 1
    while not np.array_equal(frames[i-1], frames[i]):
        next = iterate_seats(frames[i], is_floor)
        next[next < 0] = 0
        frames.append(next)
        i += 1

    print("Occupied seats: %d" % np.sum(frames[-1] > 0))

    animate_soln(frames)

