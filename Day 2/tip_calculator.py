print("**** Welcome to TIP Calculator")

total_bill = float(input("What was the total bill? $"))
tip = -1
while tip not in [10, 12, 15]:
	tip = int(input("What tip percentage would you like to give? "))

people_count = int(input("How many people should the bill get split into? "))

your_bill = (total_bill * (100 + tip) / 100.0) / people_count

print("Each person should pay: $" + str(your_bill))