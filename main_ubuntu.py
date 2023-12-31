# Description:  Program converts pdf file_folders in a given directory, converts them to png file_folders, and deletes the pdfs

from pdf2image import convert_from_path
import subprocess
from pathlib import Path
import os
import re

pdf_directory = "file_folders/pdfs"
pic_directory = "file_folders/pictures"
files = os.listdir(pdf_directory)
new_picture_list = []


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
        new_pic = convert_from_path(pdf_directory+"/"+pdf, output_file=short3, output_folder=pdf_directory, fmt=".PNG")

for i in range(len(files)):
    pdf = files[i]
    file_name = os.path.basename(pdf)
    extension = Path(file_name).suffix
    if file_name in files and extension == ".pdf":
        # print('')
        delete = os.remove(pdf_directory + "/" + file_name)     # deletes pdf file_folders when job is complete
    elif extension != ".pdf":
        print(file_name, "was not completed because it is not a pdf")

new_files = os.listdir(pdf_directory)     # gets the contents of the file folder after conversion


def display_pop_up():
    for i in new_files:
        file_path = os.path.join(pdf_directory, i)
        subprocess.run(["xdg-open", file_path], check=True)

def display_choice():
    display_input = input("Would you like to display the converted image? (yes/no) ")
    match display_input:
        case 'yes' | "Yes" | "y" | "Y":
            display_pop_up()
        case 'no' | "No" | "n" | "N":
            print("Conversion Finished")
        case _:
            print("Not a valid input")
            display_choice()

display_choice()
