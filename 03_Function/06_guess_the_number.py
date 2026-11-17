import random

flag = 0

def guess_number(num):
    global flag
    for i in range(3):
        print("Try to Guess the number!")
        guess = int(input("Enter number between 1 to 20: "))
        
        if(guess < num):
            print("The number you guessed too low")
        elif (guess > num):
            print("The number you guessed is too high")
        else:
            flag = 1
    return guess 

def check_num(secret):            
    if flag:
        print("Congratulations! You have guess the number")        
    else:
        print("Better luck next time!! The secret number was ", secret)


if __name__ == "__main__":
    secret_num = random.randint(1, 20)
    print("I am currently thinking of a number.")
    guessed_num = guess_number(secret_num)
    check_num(secret_num)