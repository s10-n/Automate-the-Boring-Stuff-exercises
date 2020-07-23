alsTableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
# find the longest string of each inner list
def printTable(tableData):
    def longestString(tableData):
        colWidths = []
        for category in tableData:
            longestWord = 0
            for i in range(len(category)):
                if len(category[i]) > longestWord:
                    longestWord = len(category[i])
            colWidths.append(longestWord)
        return colWidths
    colWidths = longestString(tableData)
    for word in range(len(tableData[0])):
        for category in range(len(tableData)):
            print(tableData[category][word].rjust(colWidths[category],' ') + ' ',end='')
        print('\n')
printTable(alsTableData)
