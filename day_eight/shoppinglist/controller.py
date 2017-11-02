from view import View
from model import Database

#Open connection to database with the Database class from models
my_database = Database()

#Initialize View class from view
my_view = View()

running = True
#Run menu until the exit choice is selected
while running == True:
	#output menu and take user input
	user_input = my_view.menu()

	#Insert item into shoppinglist
	if user_input == "1":
		#Get item name
		list_item = my_view.takeInput("Enter the name of the item: ")

		#Get amount of item
		choosing = True
		amount_of_item = ""
		while choosing == True:
			amount_of_item = my_view.takeInput("Enter how many of that item you want: ")

			#CHeck if input is integer and convert to interger
			if amount_of_item.isdigit() == True:
				amount_of_item = int(amount_of_item)
				choosing = False
		
		#insert item into database
		my_database.insertIntoDatabase(list_item, amount_of_item)

	#Show all items on list
	elif user_input == "2":
		#Get all items as a list of tuples with the order (ID, item_Name, amount_of_item, checked)
		item_list = my_database.selectFromDatabase()

		#Print out legend of table
		my_view.printOut("ID \t| item \t|amount\t| checked")
		#Print out each row of the table
		for item in item_list:
			my_view.printTableRow(item)

	#CHeck off item on list
	elif user_input == "3":

		#CHoose a valid ID to check off
		choosing = True
		while choosing == True:
			item_id = my_view.takeInput("Enter a id to check off: ")

			#Check if input is an ID
			if item_id.isdigit() == True:
				item_id = int(item_id)

				#Get all ids as a list of integers
				list_of_ids = my_database.getIds()

				#If table is empty alert user that table is empty and you cant check off an empty list
				if list_of_ids == []:
					choosing = False
					my_view.printOut("No items on list.")

				#IF input matches a id then update the row with that id to be checked
				elif item_id in list_of_ids:
					my_database.updateChecked(item_id, "CHECKED")
					choosing = False

				#Alert user that that is not a valid id.
				else:
					my_view.printOut("That ID is not on the list. Try again")


	#Uncheck item. Same as number 3 only sets to UNCHECKED instead of CHECKED
	elif user_input == "4":

		choosing = True
		while choosing == True:
			item_id = my_view.takeInput("Enter a id to check off: ")

			if item_id.isdigit() == True:
				item_id = int(item_id)

				list_of_ids = my_database.getIds()

				if list_of_ids == []:
					choosing = False
					my_view.printOut("No items on list.")

				elif item_id in list_of_ids:
					#Only difference is "UNCHECKED"
					my_database.updateChecked(item_id, "UNCHECKED")
					choosing = False

				else:
					my_view.printOut("That ID is not on the list. Try again")

					
	#Exit menu and program
	elif user_input == "5":
		running = False
		my_view.printOut("Thank you for using my program")
	#Alert user to invalid selection
	else:
		my_view.printOut("That is not a valid choice, try again.")