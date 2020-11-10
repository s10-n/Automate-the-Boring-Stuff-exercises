#! python3
# textMyself.py - defines the textmyself() function that texts a message passed to it as a string
import textMyselfValues
def textmyself(message):
    twilioCli = Client(accountSID,authToken)
    twilioCli.messages.create(body=message, from_=textMyselfValues.twilioNumber, to=textMyselfValues.myNumber)
