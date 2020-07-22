import random
numberOfStreaks = 0
numberOfExperiments = 10000
for experimentNumber in range(numberOfExperiments):
    tossList = []
    for toss in range(100):
        tossList += [random.randint(0,1)] # create a list of 100 random values
    streak = 1
    for i in range (1,len(tossList)):
        if tossList[i] == tossList[toss-1]:
            streak+=1
        else:
            streak = 1
        if streak == 6:
            numberOfStreaks += 1
            break
            # Code that checks if there is a streak of 6 heads or tails in a row.
print('Chance of streak: %s%%' % (numberOfStreaks / 100))