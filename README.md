# PDF File Merger
Merges few pdf files together.

# Table of contents
* [Introduction](#introduction)
* [Technologies](#technologies)
* [Setup](#setup)
* [How to use](#how-to-use)

# Introduction
PDF File Merger is a simple Python program with GUI to merge pdf files. User can add, delete and move pdf files in the list via buttons. Order the files from top to bottom. The file at the top will be the first file in the final pdf. The goal of this project was to write an easy-to-use tool to merge pdf files which is not an easily accessible function.

![Alt text](/images/main.png?raw=true "Main window")

# Technologies
All code is written in Python 3.7.6. The program uses two modules:
- tkinter (standard) - to generate the GUI
- PyPDF2 (non-standard) to operate on pdf files.

The code was tested on Windows 10

# Setup
No setup is necessary. Ensure you have all essential modules and run main.py

# How to use
Use button 'Add' to add pdf files to the list. The program will prompt you to choose a file through a browse window. Delete files from the list by selecting a position and clicking 'Delete' button. Use 'To top' and 'To bottom' buttons to change the order on the list. Merging process will add files to the final file starting from the top. When ready click 'Merge pdfs'. The program will prompt you to indicate the directory and the name of the outcome file.
