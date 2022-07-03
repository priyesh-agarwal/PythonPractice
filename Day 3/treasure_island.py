print("************************************")
print(r'''
       ____  __.---""---.__  ____
      /####\/              \/####\
     (   /\ )              ( /\   )
     \____/                \____/
    __/                          \__
 .-"    .                      .    "-.
 |  |   \.._                _../   |  |
  \  \    \."-.__________.-"./    /  /
    \  \    "--.________.--"    /  /
  ___\  \_                    _/  /___
./    )))))                  (((((    \.
\                                      /
 \           \_          _/           /
   \    \____/""-.____.-""\____/    /
     \    \                  /    /
      \.  .|                |.  ./
    ." / |  \              /  | \  ".
 ."  /   |   \            /   |   \   ".
/.-./.--.|.--.\          /.--.|.--.\.-.|
''')
print("************************************")

print("\nWelcome to Treasure Island")
print("Your mission is to find the treasure.")

choice1 = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\"\n").lower()

if choice1 != "left":
	print("A truck hit you!! You die.")
else:
	choice2 = input("You come to a lake. There is an island in the middle of the laje. Type \"wait\" to wait for a boat. Type \"swim\" to swim across\n")
	if choice2 != "wait":
		print("A crocodile was waiting for it's prey for so long. Finally you arrived. Game Over! You die.")
	else:
		choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n")
		if choice3 == "blue":
			print("You enter a room of beasts. Game Over")
		elif choice3 == "red":
			print("You enter a room of snakes. Hiss!! Game Over")
		else:
			print("You found the treasure! Congrats you won the game.")


