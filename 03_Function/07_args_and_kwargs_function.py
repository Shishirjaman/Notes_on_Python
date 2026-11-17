# function with *args
# We use *args when we don't know how many positional arguments
# will be passed to a function.
# *args is worked like list in python.

def calculate(*numbers):
    total = 0

    for number in numbers:
        total += number

    return total


if __name__ == "__main__":
    print(calculate(10, 20))
    print(calculate(10, 20, 30))
    print(calculate(10, 20, 30, 40))

# --------------------------------- ######### ----------------------------------
# function with **kwargs
# We use **kwargs when we don't know how many 
# keyword arguments will be passed to a function. 
# **kwargs is worked like dictionary in python.
   
def student_info(**details):

    for key, value in details.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    student_info(
        name="Shishir",
        age=27,
        department="Computer Science",
        university="Bishop's University"
    )