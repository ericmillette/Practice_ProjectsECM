
#random walk: 1-dimensional either (-1, 0) or (1, 0) within n iterations (blocks)
import random
from statistics import mean

def random_walk(num_blocks): # n = number of blocks traveled
    x = 0
    for i in range(num_blocks):
        a = random.choice([1, -1])
        x += a
    return x

def simulation(num_blocks):
    num_walks = int(input("How many walks would you like to simulate?: "))
    avg_walk = []
    for i in range(num_walks):
        avg_walk.append(random_walk(num_blocks))
        print(f"you've traveled {abs(avg_walk[i])} block(s) from home")
    print(f"on average, you walked {mean(avg_walk)} blocks from home")

simulation(int(input("How many blocks would you like to randomly walk?: ")))