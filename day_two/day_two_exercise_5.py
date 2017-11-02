number = int( input("Enter a number: ") )

#Dictionary with integers as keys and the equivalent roman numeral as a value
number_to_roman = {1000:"M",900:"CM",500:"D",400:"CD",100:"C",90:"XC",50:"L",40:"XL",10:"X",9:"IX",5:"V",4:"IV",1:"I"}

#The keys of our dictionary in descending order
keys = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

#The new number as a roman number
roman = ""

# run until all numbers have been converted into roman numerals
while number > 0:
	#We need to check what the largest roman numeral is that fits in out current number
	for divisor in keys:
		#If the number divided by the divisor is not equal to the original number then we know divisor is the largest roman number that fits in number

		if number % divisor != number:
			#Reduce number by the divisor and add the roman numeral to the new string roman
			roman = roman + number_to_roman[divisor]
			number = number - divisor
			#End the for loop because only one roman numeral can be added at a time
			break



print(roman)