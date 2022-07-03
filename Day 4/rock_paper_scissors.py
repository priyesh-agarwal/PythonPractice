rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

options = [rock, paper, scissors]

import random

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for scissors\n"))
print(options[choice])

oppenent_choice = random.randint(0,2)
print("Computer Chose:\n" + options[oppenent_choice])

all_possibilities = [(0,0,0),(0,1,-1),(0,2,1),(1,1,0),(1,2,-1),(2,2,0)]

match_result = -2

for possibility in all_possibilities:
	if choice == possibility[0] and oppenent_choice == possibility[1]:
		match_result = possibility[2]
	elif choice == possibility[1] and oppenent_choice == possibility[0]:
		match_result = -possibility[2]

if match_result == 0:
	print("It's a Draw")
elif match_result == 1:
	print("You Won")
else:
	print("You Lose")