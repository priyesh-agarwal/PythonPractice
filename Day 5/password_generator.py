import random

print("Welcome to the PyPassword Generator!")

letters = int(input("How many letters would you like in your password? "))
numbers = int(input("How many numbers would you like? "))
symbols = int(input("How many symbols would you like? "))

char_count = letters + numbers + symbols

password = ""

def getLetter():
	letter = random.randint(1,52)
	if letter <= 26:
		return chr(letter - 1 + ord('a'))
	else:
		return chr(letter - 27 + ord('A'))

def getNumber():
	number = random.randint(0, 9)
	return chr(number + ord('0'))

def getSymbol():
	symbols = '!@#$%^&*()'
	choice = random.randint(0, len(symbols)-1)
	return symbols[choice]

for i in range(char_count):
	choice = random.randint(1, letters + numbers + symbols)
	if choice <= letters:
		password += getLetter()
		letters -= 1
	elif choice <= letters + numbers:
		password += getNumber()
		numbers -= 1
	else:
		password += getSymbol()
		symbols -= 1

print(password)