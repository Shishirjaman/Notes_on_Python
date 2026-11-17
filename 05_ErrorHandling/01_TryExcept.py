## Zero devisor error handling
a = int(input("Enter value of a: "))
b = int(input('Enter value of b: '))

try:
    c = a / b
    print(c)
    
except ZeroDivisionError:
    print("Can't Divide by Zero!")
    
    
## IO error handling  
try:
    fn = open('ijkl')
    fn.write("this is a text file")
    fn.close()

except IOError: # if statement in the try face the IO error then the except statement will occurs
    print("can't open that file, it doesn't exist!!")
    
else: # if statement inside try worked it will execute the else statement means if the exception doesn't occurs
    print("Everything worked well!!")
    

## if we don't know the possible error type we can just keep the except no error type required.
try:
    fd = open("myfile")
    fd.write("some string")
    fd.close()
    
except:
    print("file doesn't exist!!")
    
else:
    print("Everything worked fine!!")
    
    
## we can write multiple exception error in the following way

# try:
#      Execute Code operation.
# except (ExceptionErr1[, ExceptionErr2[, ExceptionErr3[, ...ExceptionErrN]]]):
#      this code right here execute when error occurs.
# else:
#      If there is no error that occured in the program run this part.
