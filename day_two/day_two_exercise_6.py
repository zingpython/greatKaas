


def reverseLookup(dictionary, target):

	new_dictionary = {}

	for key, value in dictionary.items():
		if target == value:
			new_dictionary[key] = value

	return new_dictionary

my_dict = {"le":"the","lui":"the","pomme":"apple"}

print( reverseLookup(my_dict, "the") )