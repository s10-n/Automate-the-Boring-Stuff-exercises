#! python3
# stopwatch.py - a simple stopwatch program
import time
# display the program's instructions
print('Press ENTER to begin. Afterward, press ENTER to click the stopwatch. Press Ctrl-C to quit.')
input()
print('Started.')
startTime = time.time()
lastTime = startTime
lapNum = 1
# start tracking the lap times
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
        lapNum += 1
        lastTime = time.time() # reset the last lap time
except KeyboardInterrupt:
    print('\nDone.')
