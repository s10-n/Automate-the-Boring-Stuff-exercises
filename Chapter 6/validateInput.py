while True:
    print('Enter your age:')
    age = input()
    if age.isdecimal():
        break
    print(f'Please enter a number for your age. "{age}" is not a number.')
while True:
    print('Select a new password (letters and numbers only):')
    password = input()
    if password.isalnum():
        break
    print('Passwords can only have letters and numbers.')