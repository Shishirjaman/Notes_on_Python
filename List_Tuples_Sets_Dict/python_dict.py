# in python, dictionary is defined by using {} and dict() method
# dictionary stores data in key value pairs
# keys must be unique and immutable
# values can be of any data types
# dictionary is unordered like set (modern python preserve insertion order)

# create an empty dictionary
dict1 = {}
dict2 = dict()

print(dict1)
print(dict2)

# assigning multiple same data types elements
dict1 = {'a': 1, 'b': 2, 'c': 3}
print(dict1)


#assigning different data types multiple elements
dict1 = {'a': 5, 1: 6, 'b': 7}
print(dict1)

dict2 = {'name':'sam', 'age':24, 'marks':95.5, 'status':'misc'}
print(dict2)

# accessing element of the dictionary by using key
print(dict2['name'])

# concatenating dictionary with string
print("the person name is "+ dict2['name'] +" and the age is "+ str(dict2['age']))

# creating nested dictionary
dict3 = {
        "student1":{"name":"John", "age":20},
        "student2":{"name":"Jane", "age":22}
         }
print(dict3)

# accessing nested dictionary values 
print(dict3['student2']['age']) 

# checking type of dict3
print(type(dict3))

# checking the number of key value pairs(length) in the dictionary
length = len(dict2)
print(length)


# ------------------------------------------------------------------------------------------ #


# adding or updating elements 
student_dict = {'name':"Max", 'age': 14, 'class': 7}
student_dict['section'] = 2
print(student_dict)

# updating existing key value
student_dict['class'] = 8
print(student_dict)

# update method for multiple additions
student_personal = {'city': 'Montreal', 'Province': 'Quebec', 'Country': 'Canada'}
student_dict.update(student_personal) # can directly put the dict inside update() method
print(student_dict)


# ------------------------------------------------------------------------------------------ #


# delete an element from dictionary
del student_dict['Province']
print(student_dict)

# delete an element using pop() method, it removes key and returns value
removed = student_dict.pop('city')
print("removed: ", removed)
print(student_dict)

# popitem(): remove last inserted pair (key, value)
pair = student_dict.popitem()
print("removed pair: ", pair)
print(student_dict)

# clear(): delete all the elements from the dictionary
temp_dict = {'x':1, 'y':2}
temp_dict.clear()
print(temp_dict) 


# ------------------------------------------------------------------------------------ #


# check to if an element exists in the list or not
# if exist it returns true else false
# checks the keys only (not value)
print('name' in student_dict)

if 'age' in student_dict:
    print("exist!!!")
else: 
    print("not exist!!!")
    
# get() method: return the value if the key exists else gives the other given value (-1)
value = student_dict.get('section', -1) # if section exist in the dict return section value else will return -1
print(value)


# ------------------------------------------------------------------------------------------------------- #


# some useful dictionary methods

# keys() method: returns all the keys of the dictionary.
# iterating through keys of the dictionary using for loop and keys() method
for k in student_dict.keys():
    print(k)

# values() method: returns all the values of the dictionary
# iterating through values of the dictionary using for loop and values() method
for v in student_dict.values():
    print(v)
    
# items(): returns all pairs(key, value) of the dictionary
# iterating through key value pairs of the dictionary using for loop and items() method
for k, v in student_dict.items():
    print(k, v)
    

# --------------------------------------------------------------------------------------- #


# converting list of tuples into dictionary
pairs = [("a",1), ("b",2), ("c",3)]
new_dict = dict(pairs)
print(new_dict)

# converting dictionary to list of keys and values
key_list = list(student_dict.keys())
value_list = list(student_dict.values())
print(key_list)
print(value_list)


# ---------------------------------------------------------------------------------------- #


# Dictionary Comprehension
# creating a dictionary with double values of a dictionary
new_dict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
double_dict = {k:v*2 for k,v in new_dict.items()}
print(double_dict)

# similarly creating dictionary by chaning keys of a dictionary
cng_dict = {k*2:v for (k,v) in new_dict.items()}
print(cng_dict)

# creating a dictionary with keys 0 to 10 even numbers(divisable by 2) and 
# values are squared of keys
num = range(10)
even_dict = {n: n**2 for n in num if n%2 == 0}
print(even_dict)

# create a dictionary from a dictionary where values are greater than 2
greater_dict = {k: v for (k,v) in new_dict.items() if v>2}
print(greater_dict)

# create a dictionary from a dictionary where values are greater than 2 and even
evgreater_dict = {k: v for (k,v) in new_dict.items() if v>2 and v%2 == 0}
print(evgreater_dict)

# create a dictionary from a dictionary where values are greater than 2 and odd
oddgreater_dict = {k: v for (k,v) in new_dict.items() if v>2 and v%2 == 1}
print(oddgreater_dict)

# swapping keys and values of a dictionary
swapped_dict = {v: k for (k,v) in new_dict.items()}
print(swapped_dict)