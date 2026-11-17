# Try: Statement code that has chance to may have error written here.
# Except: If the error occured the explation of the error code written here.
# Else: If the exception doesn't occured then what rest code what need to execute is written here.
# Finally: Exception occured or not the code that always need to run in written here.
# in short:
# try      → Try this
# except   → Something went wrong
# else     → Nothing went wrong
# finally  → Do this anyway

try:
    amount = int(input("How much do you want to withdraw? "))

    if amount > 1000:
        raise ValueError("Amount too large")

    print("Withdrawing", amount)

except ValueError as error:
    print("Error:", error)

finally:
    print("Thank you for using the ATM.")
    

# Another example using try exception finally with function.

def strNumConverter(var):
    try: 
        num = int(var)
        print("The is: ", num)
    
    except ValueError as Argument:
        print("The input given as string is not a number.\n",Argument)
        
    finally:
        print("Thank you. You can try again!")

strNumConverter('www') 