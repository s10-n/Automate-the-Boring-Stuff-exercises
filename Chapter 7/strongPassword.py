# strongPassword.py - detects whether a given password is strong

# a strong password must be at least 8 characters long, contain both uppercase and lowercase characters, and have at least one digit

import re

lengthRegex = re.compile(r'(.{8,})+')
uppercaseRegex = re.compile(r'.*[a-z].*')
lowercaseRegex = re.compile(r'.*[A-Z].*')
digitRegex = re.compile(r'.*\d.*')

# passwordValidator(password)
# takes in password, checks if it is strong
# outputs True if strong and False if not

def passwordValidator(password):
    if lengthRegex.findall(password) and uppercaseRegex.findall(password) and lowercaseRegex.findall(password) and digitRegex.findall(password):
        return True
    else:
        return False


    # test uppercase
    # test lowercase
    # test digit
    # if all true, return true

print(passwordValidator("12345678")) # False
passwordValidator("One2345678") # True
passwordValidator("one2345678") # False
passwordValidator("Poop") # False
passwordValidator("P00pcorn") # True
passwordValidator("p00pcorn") # False