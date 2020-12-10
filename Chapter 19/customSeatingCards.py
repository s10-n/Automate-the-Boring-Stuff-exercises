#! python3
# creates image invitations for guests listed in an external invite list file

import os,re
from PIL import Image, ImageDraw

# get the list of guests 
guest_file = open('guests.txt','r')
guest_list = guest_file.readlines()

for guest in guest_list:
    guest = re.sub('\n','',guest)
    print(f'Creating the invitation for {guest}...')
    # create an image
    image = Image.open('flowers.jpg')
    image_width, image_height = image.size
    # create the border
    draw = ImageDraw.Draw(image)
    draw.line([(0,0),(0,image_height-1),(image_width-1,image_height-1),(image_width-1,0),(0,0)], fill='black')
    # print the text
    message = ['It would be a pleasure to have the company of',
               guest,
               'at 11010 Memory Lane on the Evening of',
               'April 1st',
               "at 7 o'clock"]
    for line in range(len(message)):
        text_width, text_height = draw.textsize(message[line])
        text_draw_x = (image_width-text_width)/2
        text_draw_y = (image_height/2) + ((line - round(len(message)/2)) * text_height * 2)
        draw.text((text_draw_x,text_draw_y), message[line], fill='black')
    # save the image
    image.save(guest + '.png')

guest_file.close()
