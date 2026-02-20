# local variable in python function
# if we declare a variable inside the function that is considered as local
# variable. And we can't call this variable outside of the function.
# and if we declare a variable outside of the function with same name,
# still both will be two different variable having same name only.
def printString(string):
    strng = string  # strng is local variable
    print(strng)
    
    
if __name__ == "__main__":
    printString("Hi! how are you!")
    
    
# global variable in python function
# global variable declared outside of the function so it get access to the whole
# code statement means anything declared (function, main function) after the
# variable declaration
count = 0

def printCount():    
    print(f"The initial value of Count is: {count}") # count is global variable


# if we want to change the global variable inside function then we need to
# use "global" keyword. by this function understand this is global operation
# not any local operation with local variable

def numberAdd(num):
    global count
    for i in range(num):
        count += 1
        
    print(f"We need to add 1 {count} times to get the {num}")

    
if __name__ == "__main__":
    printCount()
    numberAdd(5)
    
