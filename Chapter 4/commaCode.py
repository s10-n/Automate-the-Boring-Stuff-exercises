def listToStrings(inputList):
    try:
        if len(inputList) == 1:
            print(str(inputList[0]) + '.')
        elif len(inputList) == 2:
            print(str(inputList[0]) + ' and ' + str(inputList[1]) + '.')
        else:
            for item in range(len(inputList) - 1):
                print(str(inputList[item]) + ', ',end='')
            print('and ' + str(inputList[-1]) + '.')
    except IndexError:
        print('List must have at least one entry.')

longList = []
for i in range(1,421):
    longList += [i]
shortList = [[1,2,3,4,5,6,7,8,9,20],12]


listToStrings(['pens', 'staplers', 'flamethrowers', 'binders'])
listToStrings( ['apples', 'bananas', 'tofu', 'cats'])
listToStrings(['Sammy', 'Bing'])
listToStrings(shortList)
listToStrings(longList)
