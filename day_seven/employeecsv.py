import sqlite3
import csv

#Run the createTable once and then only if the database needs to be rebuilt
def createTable():
	connection = sqlite3.connect("employee.db")

	cursor = connection.cursor()

	cursor.execute(''' CREATE TABLE employees(
		id INTEGER PRIMARY KEY,
		name VARCHAR(256),
		email VARCHAR(256),
		country VARCHAR(256)
		)''')

	cursor.execute(''' CREATE TABLE phones(
		id INTEGER PRIMARY KEY,
		phone_number VARCHAR(256),
		phone_type VARCHAR(256),
		employees_id INTEGER,
		FOREIGN KEY(employees_id) REFERENCES employees(id) 
		)
		''')

	connection.commit()

	connection.close()

# createTable()

#COnnect to the database
connection = sqlite3.connect("employee.db")

#Create a cursor in the database to manipulate the database
cursor = connection.cursor()

#Open the csv file like a text file
with open("employees.csv", newline="") as csvfile:
	#Use the CDV library to interpret the csv file
	csvlines = csv.reader(csvfile)
	#Process each line of the csv file one at a time
	for line in csvlines:
		#Create n employee based on the information from the CSV file
		cursor.execute("INSERT INTO employees(name,email,country) VALUES (?,?,?)", (line[0],line[4],line[5]) )
		#Get the id of the row just created
		lastid = cursor.lastrowid

		#Create 3 phone rows using the CSV file and the id of the new employee
		cursor.execute("INSERT INTO phones(phone_number,phone_type,employees_id) VALUES (?,?,?)", (line[1], "cellphone",lastid) )

		cursor.execute("INSERT INTO phones(phone_number,phone_type,employees_id) VALUES (?,?,?)", (line[2], "homephone",lastid) )
		
		cursor.execute("INSERT INTO phones(phone_number,phone_type,employees_id) VALUES (?,?,?)", (line[3], "workphone",lastid) )
		
		#Save the employee and phones
		connection.commit()

#Close connection to database
connection.close()