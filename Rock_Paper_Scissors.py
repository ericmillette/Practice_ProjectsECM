import random
#classes = things, functions = actions

def play():
    player = input("'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'])
    each_choice = "You chose: " + str(player) + "... computer chose: " + str(computer)

    if player not in ['r', 's', 'p']:
        exit('invalid character')

    if player == computer:
        print(each_choice)
        return 'tie'

    if is_win(player, computer):
        print(each_choice)
        return 'player wins'
    else:
        print(each_choice)
        return 'player lost, computer won'
    # r > s, s > p, p > r

def is_win(x, y):
    # return true if player wins
    if (x == 'r' and y == 's') or (x == 's' and y == 'p') or (x == 'p' and y == 'r'):
            return True

play()