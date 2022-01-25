# -*- coding: utf-8 -*-
"""
This python file accepts a folder path and converts the files in it.
Then, it saves the converted in the given new path.

Created on Mon Jan 24 21:06:34 2022

@author: Farid
"""
import sys
import os
from PIL import Image

# Grab the first and second arguments
folder_path = sys.argv[1]
new_folder_path = sys.argv[2]

# Check if the new folder path exist, if not create it
os.makedirs(new_folder_path, exist_ok=True)

# Loop through the folder, convert and save
for file in os.listdir(folder_path):
    if file.endswith(".jpg"):
        img = Image.open(f"{folder_path}/{file}")
        new_name = file.split('.')[0] + '.png'
        img.save(f"{new_folder_path}/{new_name}", 'png')
