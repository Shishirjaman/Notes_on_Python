marks = int(input("Enter your marks: "))

if marks >=90: #check the condition of if statement if condition become true then 
                #execute the codes inside if statement
    print("Great acheivement!!")
elif marks >=60: # when if statement failed (false) then check the elif statement condition
                    # when it passed (True) execute the codes inside the elif statement
    print("Passed!!")
else: 
    # when both if and elif statement failed (false) execute the codes inside the else statement 
    print("Sorry! you are failed!")