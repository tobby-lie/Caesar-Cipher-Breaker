# Caesar Cipher Code Breaker - HW1
# Tobby Lie
# CSCI 4742
# Last changed: 8/22/19 @ 6:20PM

from collections import Counter

def increment_letters(cipherText):
	"""Take in ciphertext and increment each letter of word once"""
	# Initialize string to empty string to hold value of incremented string
	new_text = ""
	# For loop to increment each character in string by one using ascii value
	for letter in cipherText:
		# Get ascii value of letter in cipherText
		ascii_value = ord(letter)
		# When ascii value reaches 123 this means it is {
		# This means ascii value needs to be reset to 140 
		# To increment to 141 which is 'a'
		if ascii_value + 1 == 123:
			ascii_value = 96
		# If letter is whitespace then skip increment and fill with space
		if letter == " ":
			new_text += " "
			continue
		# Add newly incremented character to new_text string
		new_text += chr(ascii_value + 1)
	# Return new_text in order to be used as newly incremented word
	return new_text

def increment_letters_amount(cipherText, amount):
	"""Take in ciphertext and increment each letter of word once"""
	# Initialize string to empty string to hold value of incremented string
	new_text = ""
	# For loop to increment each character in string by one using ascii value
	for letter in cipherText:
		# Get ascii value of letter in cipherText
		ascii_value = ord(letter)
		# If letter is whitespace then skip increment and fill with space
		if letter == " ":
			new_text += " "
			continue
		# Add newly incremented character to new_text string
		ascii_value += amount
		if ascii_value > 122:
			# Figure out how many ascii values out of bounds
			# The new ascii value is 
			offset = ascii_value - 122
			# The ascii value will now start at 140 (one character before 'a')
			# And increase by the offset calculated
			ascii_value = 97 + (offset - 1)
		elif ascii_value < 97:
			offset = 97 - ascii_value

			ascii_value = 122 - (offset - 1)

		new_text += chr(ascii_value)

	# Return new_text in order to be used as newly incremented word
	return new_text

def cipher_break():
	"""Loop Caesar Cipher Code Breaker code until user inputs 'y' """
	# Ask for input of cipher text to be used
	cipher_text = input("Enter ciphertext: " + "\n")
	while cipher_text == "":
		cipher_text = input("Must input ciphertext!: " + "\n")
	# Holds original text in case of any capital characters
	cipher_text_caps = cipher_text
	cipher_text = cipher_text.lower()
	# Call increment_letters in order to shift cipher text up by one letter
	cipher_text = increment_letters(cipher_text)
	# While loop continues to increment cipher text by one until user
	# Verifies that the text generated is correct
	user_input = "n"
	# Counts number of guesses
	guesses = 0
	while user_input != 'y':
		counter = 0
		# Create temporary list for cipher_text characters for
		# Manipuation with isupper()
		cipher_text_list = list(cipher_text)
		for letter in cipher_text_caps:
			if letter.isupper():
				cipher_text_list[counter] = cipher_text_list[counter].upper()	
			counter += 1
		cipher_text_list = ''.join(cipher_text_list)
		# Because of the above loop we can now print with consistency
		# Maintaining case
		user_input = input("Is it " + '"' + str(cipher_text_list) + '"?')
		user_input.lower()
 		# While input is neither y or n continue to ask for input
 		# Input validation
		while user_input not in ['y', 'n']:
 			user_input = input("Please input either y or n!")
 			user_input = user_input.lower()
 		# If text is incorrect, then need to increment
		cipher_text = cipher_text.lower()
		cipher_text = increment_letters(cipher_text)
		guesses += 1
	return guesses

def cipher_break_frequency():
	# Create list of letters in order of most used to least used
	# Based on letterfrequency.org 
	frequent_alpha = ['e', 't', 'a', 'o', 'i', 'n', 's', 'r', 'h', 'l', 'd',
		'c', 'u', 'm', 'f', 'p', 'g', 'w', 'y', 'b', 'v', 'k', 'x', 'j', 'q', 'z']

	# Ask for input of cipher text
	cipher_text = input("Enter ciphertext: " + "\n")
	while cipher_text == "":
		cipher_text = input("Must input ciphertext!: " + "\n")
	# Holds original text in case of any capital characters
	cipher_text_caps = cipher_text
	cipher_text = cipher_text.lower()
	# Turn string into list in order to traverse by index
	cipher_text_list = list(cipher_text)

	# Count most frequent appearing character in cipher_text
	occurence_count = Counter(cipher_text_list)
	most_frequent = occurence_count.most_common(2)
	key =  most_frequent[0][0]
	if key == " ":
		key = most_frequent[1][0]

	# Increment word by first letter in list based on
	# Most common letter in cipher_text
	count = 0
	found = False
	for index, alpha in enumerate(frequent_alpha):
		count += 1
		offset = ord(frequent_alpha[index]) - ord(key)

		new_word = increment_letters_amount(cipher_text, offset)

		counter = 0
		# Create temporary list for new_word characters for
		# Manipuation with isupper()
		new_word_list = list(new_word)
		for letter in cipher_text_caps:
			if letter.isupper():
				new_word_list[counter] = new_word_list[counter].upper()	
			counter += 1
		new_word_list = ''.join(new_word_list)

		user_input = input('is it "' + new_word_list + '"?')
		user_input = user_input.lower()
		while user_input not in ['y', 'n']:
 			user_input = input("Please input either y or n!")
 			user_input = user_input.lower()
		
		if user_input == 'y':
			break
	return count

def program_loop():
	"""Loop cipher_break code until user exits"""
	# Loops cipher_break until user is finished using program
	# User can exit by inputting n
	user_input = ""
	while user_input != '-1':
		prompt = "-----------------------------------\n"
		prompt += "What would you like to do?\n"
		prompt += "-----------------------------------\n"
		prompt += "1: Caesar Cipher Brute Force\n"
		prompt += "2: Caesar Cipher Frequency Attack \n"
		prompt += "-1: Exit\n"
		prompt += "(Input 1, 2 or -1 to exit):\n"
		prompt += "-----------------------------------\n"
		user_input = input(prompt)

		# Input validation for user input of choice selection
		while user_input not in ['1', '2', '-1']:
			user_input = input("Please input 1, 2 or -1 to exit!")

		if  user_input == '1':
			num_guesses = cipher_break()
			# Print out how many guesses it took
			print("-------------------------------------------\n")
			print("That took " + str(num_guesses) + " guesses!\n")
			print("-------------------------------------------\n")
		elif user_input == '2':
			num_guesses = cipher_break_frequency()
			# Print out how many guesses it took
			print("-------------------------------------------\n")
			print("That took " + str(num_guesses) + " guesses!\n")
			print("-------------------------------------------\n")
		elif user_input == '-1':
			print("-----------------------------\n")
			print("Thanks for using the program!\n")
			print("-----------------------------\n")


# Only need to have one function call to run program
program_loop()