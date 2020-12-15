#! python3
# textFromWindow.py - takes in the name of a window and returns the text within said window
import pyautogui,pyperclip

def text_from_window(window_name):
    window = pyautogui.getWindowsWithTitle(window_name)[0] # get the desired window object
    window_coordinates = window.topleft # get the window's coordinates on the screen
    if not window.isActive: # activate the window if it isn't active already
        window.activate()
    pyautogui.click(window_coordinates[0]+100, window_coordinates[1]+100) # click in the body of the window
    pyautogui.hotkey('ctrl','a') # select all
    pyautogui.hotkey('ctrl','c') # copy
    return pyperclip.paste() # paste the clipboard into the function's return value
