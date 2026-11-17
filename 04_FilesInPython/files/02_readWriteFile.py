import os

# changing directory and checking directory is changed or not
os.chdir('E:\\Python\\CodeRed_Python\\files_python\\files')
print(os.getcwd())

# opening an existing file 
file = open('file.txt')

# closing an existing opened file
file.close()

# opeing file in read(r), write(w) and append(a) mode
# in read mode
fn = open('file.txt', 'r')
print(fn.read())
fn.close() # always need to close file after operation otherwise the file will be blank

# in write mode
fn = open('file.txt', 'w')
string = "Je m'apple Shishir!"
fn.write(string) # but it will remove the existing text in the file and write the 'string' text
fn.close() # always must need to close after operation

# in append mode
fn = open('file.txt', 'a')
fn.write(" J'habit a Sherbrooke.") # it will append the new text after existing text in the file
fn.close() # always must need to close

# we can also read file in text(by default read is in text mode) and byte mode. same for write and append
# reading in text mode
fn = open('file.txt','rt')
print(fn.read()) # by default 'r' also in text mode read
fn.close()

# reading in byte mode
fn = open('file.txt', 'rb')
print(fn.read()) # extra 'b' in the beginning indicates it is in byte mode
fn.close()

# for reading file line by line
fn = open('file.txt', 'r')
for line in fn.readlines(): #by default readlines add a new line at the end of the line. 
    print(line)    
fn.close()

# to avoid by default new line after each line
fn = open('file.txt', 'r')
for line in fn.readlines():
    line = line.strip("\n")
    print(line)     
fn.close()   

# to read just one line at a time from the text file
fn = open('file.txt', 'r')

for i in range(5):
    print(fn.readline().strip('\n'))
fn.close()