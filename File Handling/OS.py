# os.getcwd() — Current Folder

import os

current_folder = os.getcwd()

print(current_folder)

# os.mkdir - Make Folder

import os

os.mkdir("New Folder") # error if folder already exists

# os.rename() - Rename

import os

os.rename("New Folder", "New Python Folder")

# os.remove() - Deletes a file

import os

os.remove("test.txt") # it deletes the file

# os.rmdir() - Deletes an empty folder

import os

os.rmdir("New Python Folder")