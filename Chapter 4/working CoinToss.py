import random
numberOfStreaks = 0
streakLength = int(input())
for experimentNumber in range(10000):
    tossList = []
    streak = 1
    for toss in range(100): # Code that creates a list of 100 'heads' or 'tails' values.
        tossList += [random.randint(0,1)]
    for i in range(1,len(tossList)): # Code that checks if there is a streak of 6 heads or tails in a row.
        if tossList[i] == tossList[i - 1]:
            streak += 1
            if streak == streakLength:
                numberOfStreaks += 1
                break
        else:
            streak = 1
print('Chance of streak: %s%%' % (numberOfStreaks / 100))