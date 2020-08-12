import re

dateRegex = re.compile(r'([0-2][0-9]|3[0-1])/(0[1-9]|1[0-2])/([1-2][0-9][0-9][0-9])')

text = 'One example of a date is 31/02/2012. Another one might be 23/11/1456. Finally, yet another date which I can look for in here is 31/01/2388. This date is not valid because the year is off: 23/02/3010, and this date is off because of the month: 05/34/2020. But wait, there\'s more! How about 11/08/2020'

days30 = ['04','06','09','11']
days28 = ['02']

validDates = []

for group in dateRegex.findall(text):
    day, month, year = int(group[0]), group[1], int(group[2])
    def isValidYear(day,month,year):# detect if it's a leap year
        if year % 4 != 0: 
            isLeapYear = False
        elif year % 100 != 0:
            isLeapYear = True
        elif year % 400 != 0:
            isLeapYear = False
        else:
            isLeapYear = True
    # detect if the date is valid for the month
        if str(month) in days30 and day > 30:
            return False
        if str(month) in days28:
            if day > 28 and isLeapYear == False:
                return False
            elif day > 29 and isLeapYear == True:
                return False
        return True
    if isValidYear(day,month,year) == True:
        validDates.append('%s/%s/%s'%(day,month,year))
print('Valid dates in text (dates use DD/MM/YYYY convention):')
for i in validDates:
    print(i)          
