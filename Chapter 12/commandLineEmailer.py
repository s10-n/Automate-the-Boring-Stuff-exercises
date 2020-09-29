#! python3
# commandLineEmailer.py - takes an email address and string of text on the command line and then, using selenium, logs in to your email account and sends an email of the string to the provided address

import sys,pyinputplus,requests,bs4
from selenium import webdriver
#if len(sys.argv) != 3:
#    raise Exception('commandLineEmailer requires an email address and a string of text.')
#else:
def command_line_emailer(email_address,email_string):
    email_provider = input('Please enter the URL of your email provider: ')
    browser = webdriver.Firefox()
    browser.get(email_provider)
    browser.find_element_by_xpath('//*[@title="Login"]').click()
    user_element = browser.find_element_by_id('login-username-input')
    user_element.send_keys(input('Please enter your email address: '))
    password_element = browser.find_element_by_id('login-password-input')
    user_password = pyinputplus.inputPassword('Please enter your password: ')
    print(user_password)

#command_line_emailer(sys.argv[1],sys.argv[2])


