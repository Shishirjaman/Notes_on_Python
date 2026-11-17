# in python, list is defined by using [] and list() method
# list can contain multiple elements of same data types and
# also can contain different data types.

# create an empty list
list1 = []
list2 = list()

print(list1)
print(list2)

# assigning multiple same data types elements
list1 = [1,2,3,4,5,6]
print(list1)
list1 = ["bat", 'cat', 'elephant', 'lion']
print(list1)

# assigning different data types multiple elements
list2 = ["sam", 24, 95.5, True, None]
print(list2)

# Indexing list: we can take an single element from the list by using index
# list index start from 0 

# printing "elephant" from the list1 
element = list1[2] # elephant placed in 3rd position
print(element) 

# checking type of list1 and element
print(type(list1))
print(type(element))

# we can concatenate list elements with string
print('This animal is an '+ list1[2] +' and not a '+ list1[-1]) # -1 means last element 

# creating empty nested list
list3 = [[],[]]
list4 = [list(), list()]

print(list3)
print(list4)

# nested list with data
list3 = [[1,2,3,4,5,6], ["bat", 'cat', 'elephant', 'lion']]
print(list3)

# accessing element of nested list
# printing cat
print(list3[1][1]) # 2nd list and 2nd element of the nested list

# printing lion
print(list3[1][-1]) # 2nd list last element of the nested list


# --------------------------------------------------------------------------------------------------- #

# slicing list by using index
new_list = ['John', 'Jack', 'Jane', 1, 2, 3, 4, 5]

# creating a new list only with names from the "new_list"
name_list = new_list[0:3] # from index 0 to before 3 [0,1,2]
print(name_list)

# if start from 0 index then we can do that without mentioning the start
name_list = new_list[:3] # this is also from index 0 to 2
print(name_list)

# creating list with numbers from "new_list"
number_list = new_list[3:8] # from index 3 to 7
print(number_list)

# if list go till the end then we can do that without mentioning the end
number_list = new_list[3:]
print(number_list)

# also we can slice a list by negative indexing
# create name list using negative indexing
name_list = new_list[0: -5]
print(name_list)

# checking the number of elements(length) in the list
length = len(new_list)
print(length)


# ---------------------------------------------------------------------------------------------------- #


# updating an element in list
name_list = ['John', 'Jack', 'Jane', "Adam"]
print(name_list)

name_list[3] = 'Jessica'
print(name_list)

# also we can update one index value with another index value
name_list[0] = name_list[1]
print(name_list)

# we can update one data type value with another in the same index
name_list[-1] = True 
print(name_list)

# list concatenation
animal_list = ['dog', 'cat', 'mouse', 'bird']
number_list = [1,2,3,4,5,6,7,8,9]

sum_list = animal_list + number_list
print(sum_list)

# delete an element from the list
# delete "6" from the sum list
del(sum_list[9])
print(sum_list)

# delete multiple elements from list
# delete all the numbers from sum_list
del(sum_list[4:])
print(sum_list)

# check to if an element exists in the list or not
# if exist it returns true else false
print('mouse' in sum_list)

if 'mouse' in sum_list:
    print("Exists!!!!!")
else:
    print("not exist!!!")
    
    
# ---------------------------------------------------------------------------------------------- #


# some useful list functions
new_list = ['milk', 'cheese', 'ham', 'soda']

# index() method: this returns index of the list if it exists in the list
idx_ham = new_list.index('ham')
print(idx_ham)

# append() method: add an element at the end of the list
new_list.append('water')
print(new_list)

# insert() method: add an element in the given index of the list 
new_list.insert(0, 'apple')
print(new_list)

# remove() method: remove the element from the list
# if dupliates exists it will remove the 1st occurrence only
# raise valueError if couldn't find the element
new_list.remove('ham')
print(new_list)

# sort() method: sort number or alphabet ascending order
# sort method works only when all data types are same
# for different data types in the same list in will give an error
new_list.sort()
print(new_list)

# printing all elements of the list one by one using loop
for i in new_list:
    print(i)
    
# pop() method: remove the last element from the list and returned it
popped_item = new_list.pop()
print(new_list)
print(popped_item)