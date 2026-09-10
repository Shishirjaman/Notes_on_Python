# opening a file in read mode and appending the same text in reversed order in the same file.

import os

os.chdir('E:\\Python\\CodeRed_Python\\files_python\\files')

file_name = 'textfile.txt'
fn = open(file_name, 'r')

for line in fn.readlines():
    line = line.strip('\n')
    line = line[::-1]
    print(line)
    fn.close()
    
    fn = open(file_name, 'a')
    line = '\n' + line
    fn.write(line)
    fn.close()
    
