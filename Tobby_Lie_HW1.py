# Caesar Cipher Code Breaker - HW1
# Tobby Lie
# CSCI 4742
# Last changed: 8/20/19 @ 6:55PM

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

def cipher_break():
	"""Loop Caesar Cipher Code Breaker code until user inputs 'y' """
	# Ask for input of cipher text to be used
	cipher_text = input("Enter ciphertext: " + "\n")
	cipher_text = cipher_text.lower()
	# Call increment_letters in order to shift cipher text up by one letter
	increment_letters(cipher_text)
	# While loop continues to increment cipher text by one until user
	# Verifies that the text generated is correct
	user_input = "n"
	while user_input != 'y':
 		user_input = input("Is it " + '"' + str(cipher_text) + '"?')
 		user_input.lower
 		# While input is neither y or n continue to ask for input
 		# Input validation
 		while user_input not in ['y', 'n']:
 			user_input = input("Please input either y or n!")
 			user_input = user_input.lower()
 		# If text is incorrect, then need to increment
 		cipher_text = increment_letters(cipher_text)

def program_loop():
	"""Loop cipher_break code until user exits"""
	# Loops cipher_break until user is finished using program
	# User can exit by inputting n
	user_input = ""
	while user_input != 'n':
		prompt = "Would you like to use the Caesar Cipher Code Breaker?\n"
		prompt += "(Input y or n):"
		user_input = input(prompt)
		while user_input not in ['y', 'n']:
			user_input = input("Please input either y or n!")
			user_input = user_input.lower()
		if  user_input == 'y':
			cipher_break()

program_loop()