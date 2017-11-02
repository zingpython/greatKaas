import sqlite3

class Database:

	#Open connection to database when initatilizing the class
	def __init__(self):
		self.connection = sqlite3.connect("shoppinglist.db")

		self.cursor = self.connection.cursor()

	#Create a new table in database
	def createTable(self):
		self.cursor.execute('''CREATE TABLE shoppinglist(
			id INTEGER PRIMARY KEY,
			item VARCHAR(256),
			amount INTEGER,
			checked VARCHAR(12)
			) ''')

		self.connection.commit()

	#Close connection to database
	def closeDatabase(self):
		self.connection.close()

	#Insert item into database with the arguments item and amount. automatically set checked to "UNCHECKED" bu default
	def insertIntoDatabase(self, item, amount):
		self.cursor.execute("INSERT INTO shoppinglist(item,amount,checked) VALUES (?,?,?)", (item, amount, "UNCHECKED") )
		self.connection.commit()

	#Get all items from database
	def selectFromDatabase(self):
		self.cursor.execute("SELECT * FROM shoppinglist")

		return self.cursor.fetchall()

	#Gets all ids from the database as a list of integers instead of a list of tuples
	#Created after all ofhter model functions due to a need for just the IDs
	def getIds(self):
		#Get only ids from table
		self.cursor.execute("SELECT id from shoppinglist")

		#fetch all from the execute statement
		list_of_tuples = self.cursor.fetchall()

		#new list of ids
		list_of_ids = []

		#For each item in list_of_tuples insert into new list as a integer
		for item in list_of_tuples:
			list_of_ids.append( item[0] )

		#return to user new list of integers
		return list_of_ids

	#Update the checked attribute in a row deteremined by the ID
	def updateChecked(self, id, checked):
		self.cursor.execute("UPDATE shoppinglist SET checked=? WHERE id=?",(checked,id))

		self.connection.commit()

#This code will only run if you directly run model.py. Use it to create the tables once.
if __name__ == "__main__":
	my_database = Database()
	my_database.createTable()
	my_database.closeDatabase()
