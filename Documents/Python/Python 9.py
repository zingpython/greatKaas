def FConv(f): #Converts Fahrenheit to Celsius
	c = 0.0;
	c = (f-32)*(5/9);
	return c;
def CConv(c): #Converts Celsius to Fahrenheit
	f = 0.0;
	f = (c*(9/5))+32;
	return f;




f = int(input("Temperature in Fahrenheit: "));
print(FConv(f));
c = int(input("Temperature in Celsius: "));
print(CConv(c));
print(FConv(CConv(c))); #Test to check if converting to C and back to F returns the the original value
