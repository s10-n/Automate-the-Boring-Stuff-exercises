# sandwichMaker.py - asks users for their sandwich preferences

import pyinputplus as pyip
import re

def sandwichMaker():
    grandTotal = 0
    breads = {'whole wheat':1.25,'white':1,'sourdough':1.5}
    proteins = {'chicken':3, 'turkey':3.25, 'ham':3.5, 'tofu':2.75}
    cheeses = {'cheddar':1.25,'Swiss':2,'mozzarella':1.25}
    condiments = {'mayo':0.5,'mustard':0.25,'lettuce':0.5,'tomato':0.5}
    print("Welcome to Leo's.")
    # Using inputMenu() for a bread type: wheat, white, or sourdough.
    bread = pyip.inputMenu(list(breads.keys()),prompt='What kind of bread do you want your sandwich on?\n')
    grandTotal += breads[bread]
    # Using inputMenu() for a protein type: chicken, turkey, ham, or tofu.
    protein = pyip.inputMenu(list(proteins.keys()),prompt='Excellent choice. For your meat?\n')
    grandTotal += proteins[protein]
    # Using inputYesNo() to ask if they want cheese.
    cheeseYN = pyip.inputYesNo(prompt='You want cheese on that?\n',yesVal='Yeah',noVal='Nah')
    if cheeseYN == 'Yeah':
        cheese = pyip.inputMenu(list(cheeses.keys()))
        grandTotal += cheeses[cheese]
    mayoYN = pyip.inputYesNo(prompt='Mayo?\n',yesVal='Yeah',noVal='Nah')
    if mayoYN == 'Yeah':
        grandTotal += condiments['mayo']
    mustardYN = pyip.inputYesNo(prompt='Mustard?\n',yesVal='Yeah',noVal='Nah')
    if mustardYN == 'Yeah':
        grandTotal += condiments['mustard']
    lettuceYN = pyip.inputYesNo(prompt='Lettuce?\n',yesVal='Yeah',noVal='Nah')
    if lettuceYN == 'Yeah':
        grandTotal += condiments['lettuce']
    tomatoYN = pyip.inputYesNo(prompt='Tomato?\n',yesVal='Yeah',noVal='Nah')
    if tomatoYN == 'Yeah':
        grandTotal += condiments['tomato']
    quantity = pyip.inputInt(prompt='How many of those do you want?\n')
    grandTotal *= quantity
    priceRegex = re.compile(r'\d\d\.\d{1}')
    if not re.findall(priceRegex,str(grandTotal)):
        grandTotal = str(grandTotal) + '0'
    print("That'll be $%s. Cash or card?"%(grandTotal))



sandwichMaker()

# Using inputYesNo() to ask if they want mayo, mustard, lettuce, or tomato.
# Using inputInt() to ask how many sandwiches they want. Make sure this number is 1 or more