import os

# to get current path or current working directory
current_path = os.getcwd()
print(current_path)

# to change directory
os.chdir('E:\\Python\\CodeRed_Python')
current_path = os.getcwd() # verifying the path has changed or not
print(current_path)

# to create folder in the current directory
#os.makedirs('files')

# to create folder in another directory from current directory directory 
#os.makedirs('E:\\Python\\CodeRed_Python\\files_python\\'+'files')

# to create a path of the file or folder, following command can be used
path = os.path.abspath('files') # return path with current_directory + file/folder name
print(path)

# to check if a certain path is the absolute path or not
isPath = os.path.isabs('files') # not specify from root directory
print(isPath)
isPath = os.path.isabs('E:\\Python\\CodeRed_Python\\files') # specify from root directory
print(isPath)

# to get file name from the path
file_path = 'E:\\Python\\CodeRed_Python\\files_python\\files\\file.txt'
file_name = os.path.basename(file_path)
print(file_name)

# Similarly to get file directory path from root directory
root_path = os.path.dirname(file_path)
print(root_path)

# split can be used to get directory path from root directory and file name
# returns tuple of (dirname, basename)
dir_base_name = os.path.split(file_path)
print(dir_base_name)
directory, filename = os.path.split(file_path)
print('The path of the file '+filename+' is at this path: '+directory)

# to get size of the file in bytes (txt, mp3 and anyothers)
filesize = os.path.getsize(file_path)
print(filesize)

# to check all the files in the current directory
import subprocess
print(subprocess.check_output('dir', shell=True))

# to check if a file exist in the current directory
isexist = os.path.exists('python_basic')
print(isexist)
isexist = os.path.exists('files')
print(isexist)

# to check whether it is a name of the directory in the current directory or not
isdirectory = os.path.isdir('files_python') # if nothing exists in this name it will return false as well.
print(isdirectory)
isdirectory = os.path.isdir('files')
print(isdirectory)

# Similarly to check whether it is a name of the file in the current directory or not
file = os.path.isfile('files_python\\files\\file.txt') # if nothing exists in this name it will return false as well.
print(file)