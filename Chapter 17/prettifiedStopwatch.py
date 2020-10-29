#! python3
# prettifiedStopwatch.py - a (slightly less) simple stopwatch program
import time,pyperclip
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
        lapNumString = str(lapNum).rjust(2)
        lapTime = round(time.time() - lastTime, 2)
        lapTimeString = str(lapTime).rjust(6)
        totalTime = round(time.time() - startTime, 2)
        totalTimeString = str(totalTime).rjust(6)
        outputString = f'Lap #{lapNumString}: {totalTimeString} ({lapTimeString})'
        print(outputString, end='')
        pyperclip.copy(outputString)
        lapNum += 1
        lastTime = time.time() # reset the last lap time
except KeyboardInterrupt:
    print('\nDone.')

    Lap # 1:   3.56 (  3.56)
