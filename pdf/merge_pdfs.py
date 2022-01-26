# -*- coding: utf-8 -*-
"""
This file merges pdfs, given as arguments in the console.


Created on Tue Jan 25 21:02:40 2022

@author: Farid
"""
import sys
import os
import PyPDF2


def merge_pdfs(pdf_list):
    """
    Merges the pdfs list.

    Parameters
    ----------
    pdf_list : list
        List of paths to the requested pdfs.

    Returns
    -------
    None.

    """
    # Create a merger object
    merger = PyPDF2.PdfFileMerger()

    # Loop over the input and append to the object
    for pdf in pdf_list:
        merger.append(pdf)

    # Write into a new pdf
    merger.write('combined_pdf.pdf')


inputs = sys.argv[1:]

# check if a pattern was given.
if len(inputs) == 1 and '*' in inputs[0]:
    directory = inputs[0].split('*')[0]
    if directory == '':
        directory = os.getcwd()
    inputs = []
    for file in os.listdir(directory):
        if file.endswith('.pdf'):
            inputs.append(os.path.join(directory, file))

merge_pdfs(inputs)
