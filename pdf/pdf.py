# -*- coding: utf-8 -*-
"""

Created on Tue Jan 25 20:37:48 2022

@author: Farid
"""
import PyPDF2

with open('dummy.pdf', 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)

    print(reader.numPages)
    
# Rotate a page
with open('dummy.pdf', 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    page = reader.getPage(0)
    # Rotate
    page.rotateCounterClockwise(90)
    # Write
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('tilt.pdf', 'wb') as new_file:
        writer.write(new_file)