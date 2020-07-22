print('How many times do you want to loop this?')
loopNumber = int(input())
for i in range(loopNumber):
    if i > 10:
        print('Okay, too much.')
        break
    else:
        print('Jimmy Five Times (' + str(i) + ')')

total = 0
for num in range(101):
    total = total + num
print(total)

total = 0
count = 0
while count < 101:
    total = total + count
    count = count + 1
print(total)
