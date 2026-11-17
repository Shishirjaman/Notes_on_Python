# A lambda function is a small, anonymous(without function name & def) function 
# that can contain only one expression.
# It is defined using the lambda keyword.
# It can contain only one expression. The expression's result is automatically returned.
# We don't need to write return.

# basic lambda function to calculate square of a number

square = lambda number: number ** 2


if __name__ == "__main__":
    print(square(5))

# ---------------------------------------- ########## ------------------------------------

# lambda function with multiple parameter

# Addition of numbers
add = lambda a, b: a + b

if __name__ == "__main__":
    print(add(10, 20))
    print(add(50, 30))
    
# Multiplication of numbers
multiply = lambda a, b: a * b

if __name__ == "__main__":
    print(multiply(5, 4))
    print(multiply(10, 3))
    
# ---------------------------------------- ############ ---------------------------------------

# lambda function with condition expression

# finding the largest number
get_largest = lambda a, b: a if a > b else b

if __name__ == "__main__":
    print(get_largest(10, 20))
    print(get_largest(50, 30))
    
# ---------------------------------- ################ ----------------------------

# lambda function with default parameters

greet = lambda name="Shishir": f"Hello, {name}!"

if __name__ == "__main__":
    print(greet())
    print(greet("Rahim"))
    
# -------------------------------- ########### -------------------------

# lambda function with map()

numbers = [1, 2, 3, 4, 5]

result = map(lambda number: number ** 2, numbers) #(function, iterable)

if __name__ == "__main__":
    print(list(result))
    
# -------------------------------- ########## -------------------------

# lambda function with filter()

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = filter(lambda number: number % 2 == 0, numbers) #(function, iterable)

if __name__ == "__main__":
    print(list(result))
    
# --------------------------------- ################ ---------------------------

# lambda function with sorted()

students = [
    ("Rahim", 85),
    ("Karim", 70),
    ("Shishir", 95),
    ("Hasan", 80)
]

# sorting on ascending order
result = sorted(students, key=lambda student: student[1]) # student[1] means student marks, so sort on marks

if __name__ == "__main__":
    print(result)
    
# sorting on descending order
result = sorted(students, key=lambda student: student[1], reverse=True)

if __name__ == "__main__":
    print(result)