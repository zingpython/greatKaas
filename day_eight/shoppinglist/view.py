class View:

	#Print out the argument output
	def printOut(self, output):
		print(output)

	#Take in user input using the prompt argument
	def takeInput(self, prompt):
		return input(prompt)

	#Output menu items and take user input
	def menu(self):
		print("1. Add item to list")
		print("2. Display list")
		print("3. Check off item")
		print("4. Uncheck item")
		print("5. Exit")
		return input("Enter a Menu number: ")

	#Print a single row out
	def printTableRow(self, row):
		#Convert all integers to strings to prevent attribute error when doing string addition
		print( str(row[0])+"\t| "+row[1]+"\t| "+ str(row[2])+"\t| "+row[3])