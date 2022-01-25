# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 20:27:50 2022

@author: Farid
"""
from PIL import Image, ImageFilter

img = Image.open('./Pokedex/astro.jpg')

# Format
print(f"Image format: {img.format}")

# Size
print(f"Image size: {img.size}")

# Color Mode
print(f"Image mode: {img.mode}")

# Filter image only works when you save it as png
# filtered_img = img.filter(ImageFilter.SMOOTH)
# filtered_img.save("smooth.png",'png')

# # Grey out the image
# grayed_img = img.convert('L')
# grayed_img.save("grey.png", 'png')

# # Show the image
# grayed_img.show()

# # Rotate the image
# crooked = grayed_img.rotate(90)
# crooked.show()

# Resize the image
# resized = img.resize((300, 300))
# resized.show()

# Convert to thumbnail
img.thumbnail((400,200))
img.show()