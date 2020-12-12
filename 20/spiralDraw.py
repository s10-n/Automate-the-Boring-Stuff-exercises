import pyautogui, time
time.sleep(5)
pyautogui.click() # click to make the window active
distance = 300
change = 20
while distance > 0:
    pyautogui.drag(distance, 0, duration=0.2) # move right
    distance = distance - change
    pyautogui.drag(0, distance, duration=0.2) # move down
    pyautogui.drag(-distance, 0, duration=0.2) # move left
    distance = distance - change
    pyautogui.drag(0, -distance, duration=0.2) # move up
