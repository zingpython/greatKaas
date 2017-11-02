
message = input("Input a messag to be scrambled: ")

shift = int(input("How much do you want to shift it by? "))

new_message=""

for letter in message:
	new_letter = ord(letter)
	#Check if character is uppercase and shift accordingly
	if new_letter >= 65 and new_letter <= 90:
		#Shift character by shift number
		new_letter = new_letter + shift

		#Check if out of range of uppercase Unicode
		if new_letter >90:
			new_letter = new_letter - 26
		if new_letter < 65:
			new_letter = new_letter + 26

	#check if character is lowercase and shift accordingly
	elif new_letter >= 97 and new_letter <= 122:
		#Shift character by shift number
		new_letter = new_letter + shift

		#Check if it is out of range of lowercase Unicorde
		if new_letter >122:
			new_letter = new_letter - 26
		if new_letter < 97:
			new_letter = new_letter + 26


	new_message  =new_message + chr(new_letter)
print(new_message)