#Going shopping for school supplies
import sys
import time
import os


def animated_print(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Move to the next line

budget = 40

#first step: buy a pencil case
print("Jeff the shop owner - ")
animated_print("'Hi there! I see that you are looking for a new pencil case!'") 
print("-------------------------------")
animated_print("BUDGET = $40.00")
print("-------------------------------")
animated_print("Here are your options")
print("-------------------------------")
animated_print("1. Butterfly pencil case - $7.00")
animated_print("2. Checker pattern pencil case - $8.00")
animated_print("3. Plain white - $9.00")
animated_print("4. Plain black- $9.00")

pencil_case = int(input("Select your pencil case using the numbers, (1, 2, 3, 4): "))

if pencil_case == 1:
    budget = budget - 7
    print("Jeff the shop owner - ")
    animated_print("'Ahh I see that you are a butterfly person.")
    animated_print("Now that you have selected your pencil case,")
    animated_print("head over to the stationery section.'")
    animated_print(f"Your budget is now: ${budget}.00")
elif pencil_case == 2:
    budget = budget - 8
    print("Jeff the shop owner - ")
    animated_print("'Ooo I see you like a little bit of style.")
    animated_print("Now that you have selected your pencil case,")
    animated_print("head over to the stationery section.'")
    animated_print(f"Your budget is now: ${budget}.00")
elif pencil_case == 3:
    budget = budget - 9
    print("Jeff the shop owner - ")
    animated_print("'Ah, the classic plain white. Not a bad choice.")
    animated_print("Now that you have selected your pencil case,")
    animated_print("head over to the stationery section.'")
    animated_print(f"Your budget is now: ${budget}.00")
elif pencil_case == 4:
    budget = budget - 9
    print("Jeff the shop owner - ")
    animated_print("'Ah i see that you have chosen the plain black.")
    animated_print("Now that you have selected your pencil case,")
    animated_print("head over to the stationery section.'")
    animated_print(f"Your budget is now: ${budget}.00")
else:
    # work on while loop later
    animated_print("That is not a valid pencil case.")
    
os.system('cls' if os.name == 'nt' else 'clear')  # Windows uses 'cls', others use 'clear'
print("----------------------------------")
animated_print("*You look around and see stationery*")
print("------------STATIONERY------------")
animated_print(f"BUDGET = ${budget}.00")
print("-------------------------------")
animated_print("1. 3 pencils - $1.50")
animated_print("2. 2 pens - $5.00")
animated_print("3. 1 dust free rubber - $4.00")
animated_print("4. 1 pencil sharpener - $8.00")
animated_print("5. 4 highlighters - $9.00")
animated_print("6. 4 posca markers - $16.00")
animated_print("7. 1 mechanical pencil - $5.00")
animated_print("8. mechanical pencil lead - $3.00")
shopping_cart = []

is_running = True
while is_running:
    try:
        # Get user input and ensure it's a number
        shopping_cart_input = int(input("Select a stationery item using numbers (1 - 8): "))
    except ValueError:
        # Handle non-numeric input
        animated_print("Invalid input. Please enter a number between 1 and 8.")
        continue

    item_cost = 0
    item_name = ""

    # Match the input to an item and its cost
    if shopping_cart_input == 1:
        item_cost = 1.50
        item_name = "3 pencils"
    elif shopping_cart_input == 2:
        item_cost = 5.00
        item_name = "2 pens"
    elif shopping_cart_input == 3:
        item_cost = 4.00
        item_name = "1 dust free rubber"
    elif shopping_cart_input == 4:
        item_cost = 8.00
        item_name = "1 pencil sharpener"
    elif shopping_cart_input == 5:
        item_cost = 9.00
        item_name = "4 highlighters"
    elif shopping_cart_input == 6:
        item_cost = 16.00
        item_name = "4 posca markers"
    elif shopping_cart_input == 7:
        item_cost = 5.00
        item_name = "1 mechanical pencil"
    elif shopping_cart_input == 8:
        item_cost = 3.00
        item_name = "mechanical pencil lead"
    else:
        animated_print("Invalid selection. Please try again.")
        continue

    # Check if the user has enough budget
    if item_cost > budget:
        animated_print("You don't have enough budget for this item. Please choose something else.")
        keep_shopping = input("Would you like to keep shopping? (y or n): ").lower()
        if keep_shopping != "y":
            is_running = False
        continue

    # Deduct the cost and add the item to the shopping cart
    budget -= item_cost
    shopping_cart.append(item_name)

    # Show current shopping cart contents
    print("-------------------------------")
    animated_print(f"Your shopping cart contains: {', '.join(shopping_cart)}")
    print("-------------------------------")
    animated_print(f"You have ${budget:.2f} remaining")
    print("-------------------------------")

    # Check if the user wants to continue shopping
    if budget <= 0:
        print("-------------------------------")
        print("You're out of budget! Shopping ends here.")
        print("-------------------------------")
        input("")
        is_running = False
    else:
        keep_shopping = input("Would you like to keep shopping? (y or n): ").lower()
        if keep_shopping != "y":
            is_running = False