#! python3
# formFiller.py - Automatically fills in the form
import pyautogui, time

formData = [{'name':'Alice','fear':'eavesdroppers','source':'wand','robocop':4, 'comments':'Tell Bob I said hi.'},
            {'name':'Bob','fear':'bees','source':'amulet','robocop':4, 'comments':'n/a'},
            {'name':'Carol','fear':'puppets','source':'crystal ball','robocop':1, 'comments':'Please take the puppets out of the break room.'},
            {'name':'Alex Murphy','fear':'ED-209','source':'money','robocop':5, 'comments':'Protect the innocent. Serve the public trust. Uphold the law.'}
            ]

pyautogui.PAUSE = 0.5
print('Ensure that the browser window is active and the form is loaded.')

for person in formData:
# give the user a chance to kill the script
    print('>>> 5-SECOND PAUSE TO LET USER PRESS CTRL-C<<<')
    time.sleep(5) # wait until the form page has loaded

    print('Entering %s info...' % (person['name']))
    pyautogui.write(['\t','\t'])
    
    # fill out the Name field
    pyautogui.write(person['name'] + '\t')

    # fill out the Greatest Fear(s) field
    pyautogui.write(person['fear'] + '\t')

    # fill out the Source of Wizard Powers field
    if person['source'] == 'wand':
        pyautogui.write(['down','\t'], 0.5)
    elif person['source'] == 'amulet':
        pyautogui.write(['down', 'down','\t'], 0.5)
    elif person['source'] == 'crystal ball':
        pyautogui.write(['down', 'down','down','\t'], 0.5)
    elif person['source'] == 'crystal ball':
        pyautogui.write(['down', 'down','down','down','\t'], 0.5)

    # fill out the RoboCop field
    if person['robocop'] == 1:
        pyautogui.write([' ','\t'],0.5)
    elif person['robocop'] == 2:
        pyautogui.write(['right','\t'],0.5)
    elif person['robocop'] == 3:
        pyautogui.write(['right','right','\t'],0.5)
    elif person['robocop'] == 4:
        pyautogui.write(['right','right','right','\t'],0.5)
    elif person['robocop'] == 5:
        pyautogui.write(['right','right','right','right','\t'],0.5)
   
    # fill out the Additional Comments field
    pyautogui.write(person['comments'] + '\t')

    # click submit
    time.sleep(0.5) # wait for the button to activate
    pyautogui.press('enter')
    
    # wait until form page has loaded
    print('Submitted form.')
    time.sleep(5)
