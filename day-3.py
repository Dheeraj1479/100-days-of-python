print("Welcome to Treasure Island")
print("Your mission is to find the treasure.")
print("Your at a cross road. Where do you wanna go?")
print("Type 'left' or 'right'")
choice1 = input()
if choice1 == 'right':
    print("You fell into a hole....Game Over")
else:
    print("Do you want to 'swim' or 'wait?'")
    choice2 = input()
    if choice2 == 'swim':
        print("Attacked by trouts....Game Over")
    else:
        print("which door you wanna go? 'red','blue' or 'yellow'")
        choice3 = input()
        if choice3 == 'red':
            print("You have been burned by fire....Game over")
        elif choice3 == 'blue':
            print("You have been eaten by beasts....Game Over")
        else:
            print("You Win!")