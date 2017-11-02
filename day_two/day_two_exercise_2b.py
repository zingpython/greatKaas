sentence = input("Enter a sentence: ")

capitalize_next = True

new_sentence = ""

for x in range( len(sentence) ):
	if sentence[x] == "." or sentence[x] == "?" or sentence[x] == "!":
		capitalize_next = True
	if sentence[x].isalpha() and capitalize_next == True:
		new_sentence = new_sentence + sentence[x].upper()
		capitalize_next = False
	elif sentence[x] == "i" and sentence[x-1] == " " and sentence[x+1] == " ":
		new_sentence = new_sentence + sentence[x].upper()
	else:
		new_sentence = new_sentence + sentence[x]

print(new_sentence)