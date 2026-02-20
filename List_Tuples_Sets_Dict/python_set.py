# in python, set is defined by using set() method
# set can contain multiple elements of same data types and
# also can contain different data types.
# note: {} is used for empty dictionary not set

# create an empty set
set1 = set()
print(set1)

# assigning multiple same data types elements
set1 = {1,2,3,4,5,6}
print(set1)
set1 = {"bat", 'cat', 'elephant', 'lion'}
print(set1)

# assigning different data types multiple elements
set2 = ["sam", 24, 95.5, True, None]
print(set2)

# duplicate values in set are automatically removed
set3 = {1, 2, 2, 3, 4, 3, 3}
print(set3)

# checking type of set3
print(type(set3))

# set is unordered so accessing elements of set 
# indexing and slicing in not possible in set.
# We can do that by converting set into list or tuple
# and after performing this task converting it back to set.

# Although we can iterate through set by using loop
for num in set3:
    print(num)
    
# checking number of elements(length) in the set
print(len(set3))

# check to if an element exists in the set or not
# if exist it returns true else false
print(3 in set3)

if 3 in set3:
    print("Exists!!!!")
else:
    print("not exists!!!")
  
    
# -------------------------------------------------------------------------------------- #


# some useful set methods
new_set = {"bat", 'cat', 'elephant', 'lion'}

# add() method: used add single element in the set
new_set.add('tiger')
print(new_set)

# update(): used to add multiple elements in the set
new_set.update(['monkey', 'zebra'])
print(new_set)

# remove(): remove the element from the set
# if could not find the element shows ValueError
new_set.remove('bat')
print(new_set)

# discard(): also remove the element from the set
# if could not find the element doesn't show any error
new_set.discard("bear")
print(new_set)

# pop(): arbitrarily remove an element from the set
new_set.pop()
print(new_set)

new_set.pop()
print(new_set)

# clear(): remove all elements from the set
temp_set = {1, 2, 3}
temp_set.clear()
print(temp_set)


# -------------------------------------------------------------------------------------- #


# set operations
set_A = {1, 2, 3, 4}
set_B = {3, 4, 5, 6}

# Union operation
print(set_A | set_B)
print(set_A.union(set_B))

# intersection operation
print(set_A & set_B)
print(set_A.intersection(set_B))

# difference operation
print(set_A - set_B)
print(set_A.difference(set_B))

# symmetric difference operation
print(set_A ^ set_B)
print(set_A.symmetric_difference(set_B))