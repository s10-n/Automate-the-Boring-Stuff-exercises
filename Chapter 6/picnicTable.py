def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth,'-'))
    for item, amount in itemsDict.items():
        print(item.ljust(leftWidth,'.') + str(amount).rjust(rightWidth))
picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies':8000}
printPicnic(picnicItems, 12, 12)