def collatz(number):
    while number != 1:
        if number % 2 == 0:  # detects even number
            number = int(number / 2)
            print(number)
        elif number % 2 == 1:  # detects odd numbers
            number = int(3 * number + 1)
            print(number)
print('Enter an integer:')
while True:
    try:
        collatz(int(input()))
    except ValueError:
        print('Invalid input. Please input an integer.')
