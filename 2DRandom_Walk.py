
#random walk: 2-dimensional walk that can go at increments of N, S, E, W
# N = (0, +1), S = (0, -1), E = (1, 0), W = (-1, 0)
import random

def random_walk(b):
    #function determines final coordinates for a 2D walk b blocks long
    x, y = 0, 0
    for i in range(b):
        (dx, dy) = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        x += dx
        y += dy
    return x, y

def simulation(w):
    #simulates w number of walks with b number of blocks per walk. Average length of walk from start calculated.
    len_fromhome = 0
    b = int(input('input number of blocks per walk: '))
    print('lets walk!')
    for i in range(w):
        walk_sim = random_walk(b)
        len_fromhome += (abs(walk_sim[0]) + abs(walk_sim[1]))
    avg_dist = len_fromhome / w
    print(f'the average walk ended {avg_dist} blocks from home')

simulation(int(input('input number of walks to simulate: ')))
