# while loop
# while loop check conditions and continue executing the code statement inside the while loop 
# untill the condition become false

a = int(input("Enter the number: "))

while a < 100:
    print("The number entered is still less than 100")
    a = a + 10
    

# for loop
# for loop also check the coditions and continue executing the code statement inside the loop
# but for loop also can take the initial value and the change (increment/ decrement)

# using for loop with range()
b = int(input("Enter the number: "))
for i in range(b):
    print("Still smaller than ",b)
    

# without using range()
num_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for num in num_list:
    print(num)
    

# also we can use the following metthods with for loop

# enumerate(): It takes a collection (like a list) and returns it as an enumerating object. 
# It yields pairs containing a count (starting from 0) and the value from the list.
tasks = ['Write Code', "Debug", "Deploy"]
for index, task in enumerate(tasks, start=1): # start = 1 means count start from 1 by default 0
    print(f'Task {index}: {task}')
    
# zip(): It aggregates elements from two or more iterables. It stops when the shortest iterable is exhausted.
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

for name, score in zip(names, scores):
    print(f"{name} scored {score}")
    
# reversed(): Sometimes you need to back it up. Instead of slicing a list with [::-1] (which creates a copy),
# reversed() is more memory-efficient.
# Returns an iterator that accesses the given sequence in reverse order.
countdown = ["Ready", "Set", "Go!"]

for word in reversed(countdown):
    print(word)
    

# sorted(): If your data is a mess, sorted() organizes it on the fly.
# Returns a new sorted list from the items in any iterable. It doesn't modify the original list.
fruits = ["banana", "apple", "cherry"]

for fruit in sorted(fruits):
    print(fruit)
    

# map(): While often used to create new lists, map() is a great way to transform data instantly inside a loop header.
# It applies a specific function to every item in an iterable. 
# Best for cleaning or converting data (like strings to integers) without a separate pre-processing step.
prices_str = ["10", "25", "40"]

# Convert to int on the fly
for price in map(int, prices_str):
    print(price * 1.1) # Adding 10% tax
    

# filter(): Similar to map(), but instead of changing the data, 
# it decides whether the data should be allowed into the loop at all.
# Runs every item through a "test" function; only items that return True are yielded to the loop.
# Best for keeping your loop body clean by handling the "if" logic in the header.
numbers = [1, 5, 12, 18, 2, 25]

# Only loop through numbers greater than 10
for n in filter(lambda x: x > 10, numbers):
    print(f"Large number: {n}")