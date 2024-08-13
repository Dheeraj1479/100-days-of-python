print("Welcome to the tip calculator!")
print("What was the total bill?")
bill = int(input("$"))
print("How much tip would you like to give?")
tip = int(input())
tip = tip / 100
print("How many people split the bill?")
num = int(input())

total_tip = bill*tip
total_bill = bill + total_tip
total_cost = total_bill / num
total_amount = round(total_cost, 2)
print(f"Each person should pay ${total_cost}")
