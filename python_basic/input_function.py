# to take user input in python input() method is being used
# by default input() method takes input as a string
num = input()
print(num)
print(type(num))

# to take other datatype user input we explicitly convert the datatype by using 
# explicit methods
num = input("Enter the number: ")
num = int(num)
print(num)
print(type(num))

float_num = float(input("Enter number:"))
print(float_num)
print(type(float_num))