# break: The statement is used to exit a loop prematurely. Once the program hits a break, 
# it stops the loop entirely and moves to the very next line of code outside that loop.
# Best for searching for an item (stopping once found) or escaping an infinite while True loop.
num = int(input("Enter number where you want to stop loop: "))
i = 0
while True:
    if (i == num):
        break
    print("Still incrementing the value of!!" + str(i))
    i += 1
    
    
# The continue statement doesn't stop the whole loop; it just tells Python to 
# "skip the rest of the code in this current turn" and jump straight to the next iteration.
# Best for filtering out "bad" data or skipping specific items without killing the whole process.
foods = ["Apple", "Broccoli", "Cheese", "Donut"]

for food in foods:
    if food == "Broccoli":
        print("--- Skipping the green stuff ---")
        continue
    print(f"Eating: {food}")