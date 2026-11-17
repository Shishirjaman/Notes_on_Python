# A recursive function is a function that calls itself to solve a problem.
# Instead of solving the entire problem in one operation, 
# a recursive function breaks the problem into smaller versions of the same problem.
# A recursive function must have two important components: (both must)
# Base case: The condition that stops the recursion.
# Recursive case: The part where the function calls itself with a smaller or simpler input.

# A function that prints numbers from 1 to 5 using recursion

def count(number):

    if number > 5:       # Base case
        return

    print(number)

    count(number + 1)    # Recursive call


if __name__ == "__main__":
    count(1)
    
# ------------------------------------------ ################# -------------------------------

# Recursive function to calculate the sum of numbers

def calculate_sum(number):

    if number == 0:       # Base case
        return 0

    return number + calculate_sum(number - 1)


if __name__ == "__main__":
    print(calculate_sum(5))
    
# ------------------------------------- ############# -----------------------------------------

# Recursive function to calculate factorial

def factorial(number):

    if number == 0 or number == 1:   # Base case
        return 1

    return number * factorial(number - 1)  # Recursive call


if __name__ == "__main__":
    print(factorial(5))

# -------------------------------------- ########### ---------------------------------------------

# Recursive function to calculate fibonacci numbers

def fibonacci(number):

    if number == 0:
        return 0

    elif number == 1:
        return 1

    return fibonacci(number - 1) + fibonacci(number - 2)


if __name__ == "__main__":

    for i in range(10):
        print(fibonacci(i), end=" ")
