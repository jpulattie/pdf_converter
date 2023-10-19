# Description:  Program converts pdf files in a given directory, converts them to png files, and deletes the pdfs

from pdf2image import convert_from_path
from pathlib import Path
import os
import re

pdf_directory = "/Users/jpulattie/PycharmProjects/pdf_converter/venv/pdfs"
pic_directory = "/Users/jpulattie/PycharmProjects/pdf_converter/venv/pictures"
files = os.listdir(pdf_directory)


def strip_number(name, count):
    """Recursively takes a string and strips the string to a given length"""
    if len(name) == count:
        return name
    else:
        file_name_short = name.rstrip(name[-1])
    return strip_number(file_name_short, count)             # recursively drops .pdf from name


for i in range(len(files)):
    pdf = files[i]
    file_name = os.path.basename(pdf)
    extension = Path(file_name).suffix

    if extension == ".pdf":
        recur_name = strip_number(file_name, len(file_name)-4)
        shortened2 = re.sub(r'Quote', '', recur_name)       # cleans up file name specifically for a batch of Quotes
        short3 = re.sub(r'1', '', shortened2)               # for business before sending to customers
        new_pic = convert_from_path(pdf_directory+"/"+pdf, output_file=short3, output_folder=pic_directory, fmt=".PNG")

for i in range(len(files)):
    pdf = files[i]
    file_name = os.path.basename(pdf)
    extension = Path(file_name).suffix
    if file_name in files and extension == ".pdf":
        delete = os.remove(pdf_directory + "/" + file_name)     # deletes pdf files when job is complete
    elif extension != ".pdf":
        print(file_name, "was not completed because it is not a pdf")

print("finished")