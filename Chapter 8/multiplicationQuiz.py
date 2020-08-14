import pyinputplus as pyip
import random,time
numberOfQuestions = 10
correctAnswers = 0
for questionNumber in range(numberOfQuestions):
    # pick two random numbers
    num1= random.randint(0,9)
    num2= random.randint(0,9)
    prompt = '#%s: %s * %s = ' % (questionNumber, num1,num2)
    try:
        # right answers are handles by allowRegexes
        # wrong answers are handled by blockRegexes, with a custom message
        pyip.inputStr(prompt,allowRegexes=['^%s$'%(num1 * num2)],blockRegexes=[('.*', 'Incorrect!')],timeout=8,limit=3)
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else:
        print('Correct!')
        correctAnswers += 1
    time.sleep(1)
print('Score: %s / %s' %(correctAnswers, numberOfQuestions))