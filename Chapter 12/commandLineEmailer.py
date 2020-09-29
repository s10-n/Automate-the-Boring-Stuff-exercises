#! python3
# commandLineEmailer.py - takes an email address and string of text on the command line and then, using selenium, logs in to your email account and sends an email of the string to the provided address

import sys,pyinputplus
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def command_line_emailer(email_address,email_string):
    
    # open Yahoo in Firefox
    browser = webdriver.Firefox()
    browser.get('http://www.yahoo.com')
    
    # click on the "Sign in" button
    browser.find_element_by_id('header-signin-link').click()
    
    # find the username input box, prompt the user to enter their email, and click sign in
    user_element = browser.find_element_by_id('login-username')
    user_element.send_keys(input('Please enter your email address: '))
    browser.find_element_by_id('login-signin').click()

    # find the password input box, prompt the user to enter their password, and click sign in
    password_element = browser.find_element_by_id('login-passwd')
    user_password = pyinputplus.inputPassword('Please enter your password: ')
    password_element.send_keys(user_password)
    browser.find_element_by_id('login-signin').click()

    # open the Mail section of Yahoo
    browser.find_element_by_id('header-mail-button').click()

    # create a new message
    browser.find_element_by_tag_name('html').send_keys('n')

    # put the recipient's email in the "to" field
    browser.find_element_by_id('message-to-field').send_keys(email_address)

    # add a subject
    browser.find_element_by_xpath('//input[@data-test-id="compose-subject"]').send_keys('Sent with commandLineEmailer.py')

    # tab down to the message body, input the included message, and send
    browser.switch_to.active_element.send_keys(Keys.TAB)
    browser.switch_to.active_element.send_keys(email_string)
    browser.find_element_by_xpath('//button[@title="Send this email"]').click()
    print('Email to ' + email_address + ' sent.')
    print('Message body: ' + email_string)
    browser.quit()
    
command_line_emailer(sys.argv[1],' '.join(sys.argv[2:]))
