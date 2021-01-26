#setting up a point that moves N S E W at random.
# after x iterations, we see how far the point is from its starting coordinate.
import random
def random_walk(n):
    #returns coordinates after 'n' block random walk.
    x = 0
    y = 0
    for i in range(n):
        step = random.choice(['N', 'S', 'E', 'W'])
        if step == 'N':
            y += 1
        elif step == 'S':
            y -= 1
        elif step == 'E':
            x += 1
        else:
            x -= 1
    return (x, y)
        #elif step == 'W':
        #    x -= 1........ this works, but the above statement is more efficient

#for i in range(25):
    #testing the walking function 25 times, each walk being 10 blockslong
#   walk = random_walk(10)
    #total change in x 'index 0 in walk' and y 'index 1 in walk
#    print(walk, "distance from home = ", abs(walk[0]) + abs(walk[1]))

def random_walk_2(n): #MORE EFFICIENT WAY OF DOING random walk 1
    x, y = 0, 0 #simpler way to designate variables using one line
    for i in range(n):
        (dx, dy) = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)]) #NSEW related to their coordinate change
        x += dx
        y += dy
    return (x, y)
#function and method below are executed separately, not connected
#for i in range(25):
#    walk = random_walk(10)
#    print(walk, "distance from home = ", abs(walk[0]) + abs(walk[1]))

number_of_walks = 10000

def run_simulation(*args, **kwargs): #using args and kwargs allows us to make a function without preemptive variables
    for walk_length in range(1, 31):
        counter = 0 #number of walks that end less than 4 blocks form start
        for i in range(number_of_walks):
            (x, y) = random_walk_2(walk_length)
            distance = abs(x) + abs(y)
            if distance <= 4:
                counter += 1
        percentage = float(counter) / number_of_walks
        print('walk size = ', walk_length, ' / % of counter = ', percentage * 100)

run_simulation()