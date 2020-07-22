 import sys
import random
win = 0
loss = 0
tie = 0
print('ROCK, PAPER, SCISSORS')
while True:
    print(str(win) + ' wins, ' + str(loss) + ' losses, ' + str(tie) + ' ties.')
    while True:
        print('Enter your move: (r)ock, (p)aper, (s)cissors, or (q)uit.')
        move = input()
        if move == 'q':
            sys.exit()
        if move == 'r' or move == 'p' or move == 's':
            break
        else:
            print('Not a valid command. Use (r)ock, (p)aper, (s)cissors, or (q)uit.')
    if move == 'r':
        print('ROCK versus...')
    if move == 'p':
        print('PAPER versus...')
    if move == 's':
        print('SCISSORS versus...')
    cpuMove = random.randint(1,3)
    if cpuMove == 1:
        print('ROCK')
        if move == 'r': #tie
            print('It is a tie!')
            tie = tie + 1
            continue
        if move == 'p': #win
            print('You win!')
            win = win + 1
            continue
        if move == 's': #lose
            print('You lose!')
            loss = loss + 1
            continue
    if cpuMove == 2:
        print('PAPER')
        if move == 'p': #tie
            print('It is a tie!')
            tie = tie + 1
            continue
        if move == 's': #win
            print('You win!')
            win = win + 1
            continue
        if move == 'r': #lose
            print('You lose!')
            loss = loss + 1
            continue
    if cpuMove == 3:
        print('SCISSORS')
        if move == 's': #tie
            print('It is a tie!')
            tie = tie + 1
            continue
        if move == 'r': #win
            print('You win!')
            win = win + 1
            continue
        if move == 'p': #lose
            print('You lose!')
            loss = loss + 1
            continue