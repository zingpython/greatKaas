
message = input("Input a messag to be scrambled: ")

shift = int(input("How much do you want to shift it by? "))

new_message=""

alpha_to_num = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26}

num_to_alpha = {1:"a",2:"b",3:"c",4:"d",5:"e",6:"f",7:"g",8:"h",9:"i",10:"j",11:"k",12:"l",13:"m",14:"n",15:"o",16:"p",17:"q",18:"r",19:"s",20:"t",21:"u",22:"v",23:"w",24:"x",25:"y",26:"z"}

for letter in message:

	#Check if the letter is uppercase, if it is sore that and make it lowercase
	is_upper = False
	if letter.isupper():
		is_upper = True
	letter = letter.lower()

	#check if the letter is in the alpha_to_num dictionary to prevent a Key not found error
	if letter in alpha_to_num.keys():

		#Convert the letter to a number and apply the shift
		letter_num = alpha_to_num[letter] + shift

		#If the new number is greater than 26 or less than 0 have it overflow to the other end of the alphabet
		if letter_num > 26:
			letter_num = letter_num - 26
		elif letter_num < 1:
			letter_num = letter_num + 26

		#Convert back to a letter
		new_letter = num_to_alpha[letter_num]

		#If it was an uppercase letter capitalize it again
		if is_upper == True:
			new_letter = new_letter.upper()

		#Add to the new string
		new_message = new_message + new_letter

	#If it is a non-letter character insert it into the new string
	else:
		new_message = new_message + letter

		
print(new_message)