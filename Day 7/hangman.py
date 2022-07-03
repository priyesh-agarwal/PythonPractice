from english_words import english_words_lower_alpha_set as words
from ascii_art import *
import random

def is_alive(state):
	return state < len(HANGMANPICS) - 1

def fill_letter(guessed_word, original_word, letter):
	new_word = ""
	for i in range(len(original_word)):
		if letter == original_word[i]:
			new_word += letter
		else:
			new_word += guessed_word[i]
	return new_word

def printWord(word):
	converted_word = ""
	for w in word:
		converted_word += w + " "
	print(converted_word)

def main():
	print(hangman_logo)
	
	word_count = len(words)
	word = list(words)[random.randint(0, word_count-1)]
	guessed_word = "_" * len(word)
	hangman_state = 0
	while (is_alive(hangman_state) and guessed_word != word):
		print("Hello")
		letter = input("Guess a letter: ").lower()
		new_word = fill_letter(guessed_word, word, letter)
		printWord(new_word)
		if new_word == guessed_word:
			print(f"You guessed {letter} but that's not in the word. You lose a life")
			hangman_state += 1
		else:
			guessed_word = new_word
		print(HANGMANPICS[hangman_state])

	if not is_alive(hangman_state):
		print("HANGMAN died. Game Over")
		print(f"The word was {word}")
	else:
		print("You Win!")

main()