import random, time, copy
WIDTH = 60
HEIGHT = 20
# create a list of list for the cells
nextCells = []
for x in range(WIDTH):
    column = [] # create a new column
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append('#') # add a living cell
        else:
            column.append(' ') # add a dead cell
    nextCells.append(column) # nextCells is a list of column lists
while True: # main program loop
    print('\n\n\n\n\n') # separate each step with new lines
    currentCells = copy.deepcopy(nextCells)
    #print currentCells on the screensize
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end = '') # print the # or space
        print() # print a new line at the end of the row


    for x in range(WIDTH):
        for y in range(HEIGHT):
            # get neighbouring coordinates
            # '% WIDTH' ensures that leftCoord is always between 0 and WIDTH - 1
            leftCoord = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT
            # count number of living neighbours
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbors += 1 # top left neighbour is alive
            if currentCells[x][aboveCoord] == '#':
                numNeighbors += 1 # top neighbour is alive
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbors += 1 # top right neighbour is alive
            if currentCells[leftCoord][y] == '#':
                numNeighbors += 1 # left neighbour is alive
            if currentCells[rightCoord][y] == '#':
                numNeighbors += 1 # right neighbour is alive
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbors += 1 # bottom left neighbour is alive
            if currentCells[x][belowCoord] == '#':
                numNeighbors += 1 # bottom neighbour is alive
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbors += 1 # bottom right neighbour is alive
            # set cell based on Conway's Game of Life rules:
            if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
                # living cells with 2 or 3 neighbours stay alive
                nextCells[x][y] ='#'
            elif currentCells[x][y] == ' ' and numNeighbors == 3:
                # dead cells with 3 neighbours become alive
                nextCells[x][y] = '#'
            else:
                # everything else dies or stays dead:
                nextCells[x][y] = ' '
    time.sleep(1)