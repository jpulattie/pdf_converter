# Name of Project

## Table of Contents

- [Overview](#overview)
- [Built With](#built-with)
- [Features](#features)
- [Contact](#contact)

## Overview

[Live demo](https://drive.google.com/file/d/1NmlKyNQ98h6AUvWT_ECFJAWmFyeMW48v/view?usp=share_link) <br>
 <br>
  I built this program to meet a common need in my holiday lighting company.  Every year I need to send out pricing quotes to my customers via text message, and I prefer to send them in a picture format.  I built this program to quickly convert a batch of pdfs to png files and delete the original pdf files.<br>
   <br>
  In building this program I learned how to route files to a directory without coding directly where the files would be on my local machine. While that approach worked for my use, it would not be transferrable to another user.  The current approach lets any user of the program get the same result.    <br>
   <br>
  One feature of this program to note is that it searches and replaces the word "Quote" in the file name.  Anyone else who uses this program may not need this to occur, but for my purposes I wanted to ensure the word was not in the file name. I also made use of a recursive function to avoid the .pdf being in the file name.  There is probably a more efficient way to accomplish this, but I kept this approach because it wortks for my purposes and runtime is not an issue with my applications of the program.<br>


### Built With

Python

## Features

Converts PDF files to PNG <br>
Removes .pdf from the file name <br>
Places PNG files into a pictures folder <br>
Deletes the original PDF <br>
Will not convert any file that is not a PDF <br>
Alerts user if the file is not converted <br>
Any file not converted is not deleted <br>
Alerts the user when program is finished running <br>


## Contact

*https://https://www.linkedin.com/in/joshpulattie817
*https://github.com/jpulattie
