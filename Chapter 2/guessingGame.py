import random
target = int(random.randint(1,20))
count = 0
guess = 0
print('I am thinking of a number between 1 and 20.')
print('You have 5 guesses.')
for count in range(1,6):
    print('Type your guess.')
    guess = int(input())
    if guess == target:
        break
    elif guess > target:
        print('Nope, too high.')
    elif guess < target:
        print('Nope, too low.')
if guess == target:
    print('Nice! You guessed it in ' + str(count) + ' guesses.')
else:
    print('Well, you tried. My number was ' + str(target) + ' .')