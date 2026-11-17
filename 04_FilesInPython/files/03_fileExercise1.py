# change the directory or move to a suitable directory then create a text file in that directory and write text.

import os
directory = input('Enter Directory (use \\\ to seperate Directories): ')
directory = directory.strip('\n')

os.chdir(directory)

file_name = input('Enter the name of the file that you want to create: ')

content_of_file = 'Hi! there.\n How are you doing?\n It is all good.'

fn = open(file_name, 'wt')
fn.write(content_of_file)
fn.close()