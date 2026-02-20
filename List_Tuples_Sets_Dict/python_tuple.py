# in python, tuple is defined by using () and tuple() method
# tuple can contain multiple elements of same data types and
# also can contain different data types.
# tuple has similar functionality like list, only difference is 
# after creating tuple we can't update the elements of tuple by default

# create an empty tuple
tuple1 = ()
tuple2 = tuple()

print(tuple1)
print(tuple2)

# assigning multiple same data types elements
tuple1 = (1,2,3,4,5,6)
print(tuple1)
tuple1 = ("bat", 'cat', 'elephant', 'lion')
print(tuple1)

# assigning different data types multiple elements
tuple2 = ("sam", 24, 95.5, True, None)
print(tuple2)

# Indexing tuple: we can take an single element from the tuple by using index
# tuple index start from 0 

# printing "elephant" from the tuple1 
element = tuple1[2] # elephant placed in 3rd position
print(element) 

# checking type of tuple1 and element
print(type(tuple1))
print(type(element))

# we can concatenate tuple elements with string
print('This animal is an '+ tuple1[2] +' and not a '+ tuple1[-1]) # -1 means last element 

# creating empty nested tuple
tuple3 = ((),())
tuple4 = tuple(), tuple()

print(tuple3)
print(tuple4)

# nested tuple with data
tuple3 = ((1,2,3,4,5,6), ("bat", 'cat', 'elephant', 'lion'))
print(tuple3)

# accessing element of nested tuple
# printing cat
print(tuple3[1][1]) # 2nd tuple and 2nd element of the nested tuple

# printing lion
print(tuple3[1][-1]) # 2nd tuple last element of the nested tuple


# --------------------------------------------------------------------------------------------------- #

# slicing tuple by using index
new_tuple = ('John', 'Jack', 'Jane', 1, 2, 3, 4, 5)

# creating a new tuple only with names from the "new_tuple"
name_tuple = new_tuple[0:3] # from index 0 to before 3 [0,1,2]
print(new_tuple)

# if start from 0 index then we can do that without mentioning the start
name_tuple = new_tuple[:3] # this is also from index 0 to 2
print(name_tuple)

# creating tuple with numbers from "new_tuple"
number_tuple = new_tuple[3:8] # from index 3 to 7
print(number_tuple)

# if tuple go till the end then we can do that without mentioning the end
number_tuple = new_tuple[3:]
print(number_tuple)

# also we can slice a tuple by negative indexing
# create name tuple using negative indexing
name_tuple = new_tuple[0: -5]
print(name_tuple)

# checking the number of elements(length) in the list
length = len(new_tuple)
print(length)


# ---------------------------------------------------------------------------------------------------- #


# The main difference between tuple and list is, we can not update
# elements of the tuple but we can for list
# So one of the way update in tuples (if in case required at any cost)
# is convert tuple to list and then update the elements and then covert
# the list back to tuple 
name_tuple = ('John', 'Jack', 'Jane', "Adam")
print(name_tuple)

name_list = list(name_tuple) # converted tuple to list
name_list[3] = 'Jessica'
print(name_list)

name_tuple = tuple(name_list)
print(name_tuple)

# also we can update one index value with another index value
name_list = list(name_tuple)
name_list[0] = name_list[1]
print(name_list)
name_tuple = tuple(name_list)
print(name_tuple)

# we can update one data type value with another in the same index
name_list = list(name_tuple)
name_list[-1] = True 
print(name_list)
name_tuple = tuple(name_list)
print(name_tuple)

# tuple concatenation
animal_tuple = ('dog', 'cat', 'mouse', 'bird')
number_tuple = (1,2,3,4,5,6,7,8,9)

sum_tuple = animal_tuple + number_tuple
print(sum_tuple)

# delete an element from the tuple
# delete "6" from the sum tuple
# tuple also doesn't support deletion so 
# we need to do same as updating
sum_list = list(sum_tuple)
del(sum_list[9])
print(sum_list)
sum_tuple = tuple(sum_list)
print(sum_tuple)

# delete multiple elements from tuple
# delete all the numbers from sum_tuple
sum_list = list(sum_tuple)
del(sum_list[4:])
print(sum_list)
sum_tuple = tuple(sum_list)
print(sum_tuple)


# check to if an element exists in the tuple or not
# if exist it returns true else false
print('mouse' in sum_tuple)

if 'mouse' in sum_tuple:
    print("Exists!!!!!")
else:
    print("not exist!!!")
    
    
# ---------------------------------------------------------------------------------------------- #


# some useful tuple functions
new_tuple = ('milk', 'cheese', 'ham', 'soda')

# index() method: this returns index of the list if it exists in the list
idx_ham = new_tuple.index('ham')
print(idx_ham)

# sorted() method: sort number or alphabet ascending order
# sorted method works only when all data types are same
# for different data types in the same list in will give an error
new_tuple = sorted(new_tuple)
print(new_tuple)

# printing all elements of the list one by one using loop
for i in new_tuple:
    print(i)