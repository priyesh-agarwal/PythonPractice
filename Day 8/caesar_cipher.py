from ascii_art import *

def modify(message, shift):
	shift = (shift % 26 + 26)
	new_message = ""
	for char in message:
		if ord(char) <= ord('Z'):
			new_ord = (ord(char) - ord('A') + shift) % 26 + ord('A')
		else:
			new_ord = (ord(char) - ord('a') + shift) % 26 + ord('a')
		new_message += chr(new_ord)
	return new_message

def encrypt(message, shift):
	return modify(message, shift)

def decrypt(message, shift):
	return modify(message, -shift)

def main():

	print(logo)

	while True:
		option = input("Type 'encode' to encrypt, Type 'decode' to decrypt:\n")
		message = input("Type your message\n")
		shift = int(input("Type your shift number\n"))
		if option == "encode":
			result = encrypt(message, shift)
		else:
			result = decrypt(message, shift)

		print(f"Here's the result: {result}")
		play_again = input("Type 'yes' if you want to go again, else print 'no'\n")
		if play_again != "yes":
			break
if __name__ == "__main__":
	main()