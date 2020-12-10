#! python3
# photoFolderDetection.py - goes through every folder on your hard drive and finds potential photo folders
import os
from pathlib import Path
from PIL import Image

for foldername, subfolders, filenames in os.walk('/'):
    num_Photo_Files = 0
    num_Non_Photo_Files = 0
    for filename in filenames:
        # Check if the file extension isn't png or jpg
        if Path(filename).suffix != '.png' and Path(filename).suffix != '.jpg':
            num_Non_Photo_Files += 1
            continue # skip to next filename
        # open image file using Pillow
        try:
            image = Image.open(os.path.join(foldername, filename))
        except:
            num_Non_Photo_Files += 1
            continue
        image_width, image_height = image.size
        # check if width and height are larger than 500
        if image_width > 500 and image_height > 500:
            # image is large enough to be considered a photo
            num_Photo_Files += 1
        else:
            # image is too small to be a photo
            num_Non_Photo_Files += 1
    # if more than half of the files were photos,
    # print the absolute path of the folder
    if num_Photo_Files > num_Non_Photo_Files:
        print(foldername)
