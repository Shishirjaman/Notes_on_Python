# in python a function is defined starting with "def" at the beggining
# and then function name that we want to give 
# (function name always start with small letter, and all should be small letter),
# after that enter and closing parenthesis() and then colon(:).
# the we right the statement in the next line with 1 tab indentation gap 
# that statement will be the function statement.
# we can pass one or more parameters inside the parenthesis
# function can return one or more variables using return statement

#importing random library
import random

def getNumber(number):
    if number == 1:
        return "The number you got is 1"
    elif number == 2:
        return "The number you got is 2"
    elif number == 3:
        return "The number you got is 3"
    elif number == 4:
        return "The number you got is 4"
    elif number == 5:
        return "The number you got is 5"

# defining main function    
if __name__ == "__main__":
    random_number = random.randint(1,5)
    print(random_number)