import random
print("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors")
computer = random.randint(0 , 2)
choice = input()
if choice == "0" and computer == 2:
    print("You win!, because the computer has chosen Scissors!")
elif choice == "0" and computer == 0:
    print("Its a draw!, because the computer has chosen Rock!")
elif choice == "0" and computer == 1:
    print("You lose!, because the computer has chosen Paper!")
elif choice == "1" and computer == 2:
        print("You lose!, because the computer has chosen Scissors!")
elif choice == "1" and computer == 0:
        print("You win!, because the computer has chosen Rock!")
elif choice == "1" and computer == 1:
        print("its a draw!, because the computer has chosen Paper!")
elif choice == "2" and computer == 2:
        print("Its a draw!, because the computer has chosen Scissors!")
elif choice == "2" and computer == 0:
        print("You lose!, because the computer has chosen Rock!")
elif choice == "2" and computer == 1:
        print("You win!, because the computer has chosen Paper!")
else:
    print("Wrong input")



