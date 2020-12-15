#! python3
# facebookMessage.py - takes in a friend's name and a message and sends them that message on Facebook Messenger
import pyautogui,webbrowser,time

def send_Facebook_message(name, message='Hello!'):
    webbrowser.open('https://www.messenger.com')
    window = pyautogui.getWindowsWithTitle('Firefox')[0] # get the desired window object
    window_coordinates = window.topleft # get the window's coordinates on the screen
    if not window.isActive: # activate the window if it isn't active already
        window.activate()
    time.sleep(5) # wait for the page to load
    pyautogui.click(window_coordinates[0]+10, window_coordinates[1]+10) # click on the window bar
    pyautogui.write(name) # write your friend's name in the search bar
    time.sleep(2) # wait for their name to load
    pyautogui.write(['down', 'enter']) # select the first result and hit enter
    pyautogui.write(message) # type in the message
    pyautogui.write(['enter']) # send the message
