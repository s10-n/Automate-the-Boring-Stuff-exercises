#! python3
# textMyself.py - defines the textmyself() function that texts a message passed to it as a string
import textMyselfValues
import twilio

def textmyself(message):
    twilioCli = twilio.rest.Client(textMyselfValues.accountSID,textMyselfValues.authToken)
    twilioCli.messages.create(body=message, from_=textMyselfValues.twilioNumber, to=textMyselfValues.myNumber)
