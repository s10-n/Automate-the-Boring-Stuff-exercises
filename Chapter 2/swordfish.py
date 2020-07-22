while True:
    print('Who are you?')
    name = input()
    if name != 'Sean':
        continue
    print('Hi, Sean. What is your password?')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')