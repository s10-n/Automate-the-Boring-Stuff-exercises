#! python3
# 2048Player.py - opens 2048 at https://gabrielecirulli.github.io/2048/ and sends up, right, down, and left keystrokes to automatically play the game
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

print('2048Player: plays 2048 with very little strategy over and over again, printing the score afterwards.' + '\n')

# open 2048 in Firefox
browser = webdriver.Firefox()
browser.get('https://gabrielecirulli.github.io/2048/')

# wait for the game to load and then select the page
time.sleep(3)
html_element = browser.find_element_by_tag_name('html')

# try to click the retry button
while True:
    try:
        retry_button = browser.find_element_by_class_name('retry-button')

        # get the current score and store it in a text variable
        current_score = browser.find_element_by_class_name('score-container').text

        # click the retry button
        retry_button.click()

        # remove the '+ x' from the current score and get the final score from the first index
        final_score = current_score.split('\n+')[0]

        # print the scores
        print('Final score: ' + final_score)
        print('Current high score: ' + browser.find_element_by_class_name('best-container').text + '\n')

    # if there is an exception when trying to click the retry button, spam the arrow keys until the retry button can be clicked successfully
    except:
        html_element.send_keys(Keys.UP)
        html_element.send_keys(Keys.RIGHT)
        html_element.send_keys(Keys.DOWN)
        html_element.send_keys(Keys.LEFT)
