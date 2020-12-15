#! python3
# lookingBusy.py - nudge your mouse cursor slightly every 10 seconds to appear active

import pyautogui, time

INTERVAL = 10 # in seconds

print('Script initialized. Mouse will move every %s seconds.' % INTERVAL)
move_left = True

while True:
    time.sleep(INTERVAL)
    if move_left:
        pyautogui.move(- 5, 0, duration=1)
        move_left = False
    else:
        pyautogui.move(5, 0, duration=1)
        move_left = True
    print(f'Mouse moved to {pyautogui.position()[0]}, {pyautogui.position()[1]}')
