message = input("Enter some text: ")

new_message = ""

is_new_sentence = True

for idx in range( len(message) ):

	if message[idx] == "." or message[idx] == "?" or message[idx] == "!":
		is_new_sentence = True

	if mesage[idx].isalpha() and is_new_sentence == True:
		new_message = new_message + message[idx].upper()
		is_new_sentence = False
	#Capitalize I
	elif message[idx] == "i":
		#Check if space before I
		if message[idx-1] == " " or message[idx-1] == "." or message[idx-1] == "!" or message[idx-1] == "?":
			#Checks to see if idx+1 is out of range
			if idx+1 >= len(message):
				new_message = new_message + message[idx].upper()
			else:
				#Check if space after I
				if message[idx + 1] == " " or message[idx + 1] == "." or message[idx + 1] == "!" or message[idx + 1] == "?":
					#Captialize I and add to new message
					new_message = new_message + message[idx].upper()
		else:
			new_message = new_message + message[idx]

	else:
		new_message = new_message + message[idx]

print(new_message)