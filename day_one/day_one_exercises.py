name = input("What is your name: ")

age = int( input("Enter your age: ") )

age = age + 5


if age > 50:
	print("Hello "+name+". Damn you are old!")
elif age <= 10:
	print("Hello "+name+". Are you old enough to be using this?")
else:
	print("Hello "+ name+". You are "+str(age)+" years old.")


grocerylist = ["Ice cram", "Beer", "Bread", 10]

grocerylist[0] = "Ice Cream"

cyphyer = {"a":1, "b":2, "c":3, "d":4}

for item in range( len(grocerylist)-1, -1):
	print( grocerylist[item] )



# Exercise 2
width = float(input("What is the width of the room: "))
length = float(input("What is the length of the room: "))

print("The area of the room is "+ str(width*length) )

# Exercise 8
for i in range(1,101):
	if i%3 == 0 and i%5==0:
		print("FizzBuzz")
	elif i%3 == 0:
		print("Fizz")
	elif i%5 == 0:
		print("Buzz")

# Exercise 10
limit = 10

for x in range(1, limit+1):

	for y in range(1, limit+1):
		print( y*x , end="\t")

	print()


# exercise 6

stars = int(input("How tall would you like this pyramid: "))

for x in range(1, stars*2):
	if x <= stars:
		for y in range(x):
			print("*",end=" ")
		print()
	else:
		difference = x - stars
		for z in range( stars-difference ):
			print("*", end=" ")
		print()

