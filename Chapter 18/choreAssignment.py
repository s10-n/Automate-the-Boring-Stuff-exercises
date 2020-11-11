#! python3
# choreAssignment.py - takes a list of people’s email addresses and a list of chores that need to be done and randomly assigns chores to people

import smtplib,random,csv,sys

# open the CSV that stores the last chores done by each roommate
last_chore_file = open('last_chore.csv','r')
last_chore_reader = csv.reader(last_chore_file)

# create a dictionary of each roommate and their last performed chore from the CSV
last_chores = {}
for row in last_chore_reader:
    last_chores[row[0]] = row[1]
last_chore_file.close()

#reopen the CSV to write the assigned chore as last week's
last_chore_file = open('last_chore.csv','w')
last_chore_writer = csv.writer(last_chore_file)

# list of chores and dictionary of roommates and their emails
chores = ['do the dishes', 'clean the bathroom', 'vacuum', 'walk the dog']
roommates = {'Test Email':'test@example.com','Firstname Lastname':'firstname.lastname@collegeuniversity.edu', 'Alan Smithee':'alan_smithee@academy.com'}

# log into your email
smtpObj = smtplib.SMTP('smtp.gmail.com',587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login('test@gmail.com',sys.argv[1])

# assign each roommate a chore and email it to them
for roommate in roommates.keys():
    last_weeks_chore = last_chores[roommate]

    # ensure that they're not assigned the same chore they were last week
    if last_weeks_chore in chores:
        chores.remove(last_weeks_chore)

    # pick a random chore and then remove it from the list to avoid assigning it twice
    chore = random.choice(chores)
    chores.remove(chore)

    # append last week's chore
    if last_weeks_chore not in chores:
        chores.append(last_weeks_chore)

    # write the roommate's assigned chore to the last_chore CSV
    last_chore_writer.writerow([roommate,chore])

    # send the roommate an email
    body = f"Subject: This weekend's chore\nHi {roommate},\nYour designated chore for this weekend will be to {chore}.\nJust as a reminder, your designated chore last week was to {last_weeks_chore}."
    print(f'Sending email to {roommates[roommate]}...')
    print(body)
    print('\n')
    sendmailStatus = smtpObj.sendmail('test@gmail.com',roommates[roommate],body)
    if sendmailStatus != {}:
        print('There was a problem.')

# close the CSV
last_chore_file.close()
