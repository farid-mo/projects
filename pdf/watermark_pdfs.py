# -*- coding: utf-8 -*-
"""
This script watermarks the given pdfs in the console as input.
Created on Tue Jan 25 21:23:24 2022

@author: Farid
"""
import sys
import os
import PyPDF2


def watermark(input_file, wrm_file):
    """
    This function watermarks all the pages of the input file.

    Parameters
    ----------
    input_file : list
        List of pdf files to be watermarked.
    wrm_file : string
        Path to the watermark pdf.

    Returns
    -------
    None.

    """
    # Find the file name
    filename = input_file.split('.pdf')[0]

    # Read the content of the input file
    reader = PyPDF2.PdfFileReader(open(input_file, 'rb'))

    # Read the content of the watermark file
    wrm_reader = PyPDF2.PdfFileReader(open(wrm_file, 'rb'))

    # Create a writer
    writer = PyPDF2.PdfFileWriter()

    # Get first page of the watermark PDF
    wrm_page = wrm_reader.getPage(0)

    # Loop over pages
    for p in range(reader.numPages):
        # Get first page of the original PDF
        page = reader.getPage(p)

        # merge the two pages
        page.mergePage(wrm_page)

        # Add the page
        writer.addPage(page)

        # Save the file
        with open(f'{filename}_watermark.pdf', 'wb') as new_file:
            writer.write(new_file)


watermark_pdf = sys.argv[1]
inputs = sys.argv[2:]

# check if a pattern was given.
if len(inputs) == 1 and '*' in inputs[0]:
    directory = inputs[0].split('*')[0]
    if directory == '':
        directory = os.getcwd()
    inputs = []
    for file in os.listdir(directory):
        if file.endswith('.pdf'):
            inputs.append(os.path.join(directory, file))

# Loop over the input list and watermark it
for pdf in inputs:
    watermark(pdf, watermark_pdf)
