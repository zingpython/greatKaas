def isFib(num):
	low = 0;
	mid = 1;
	hi = 1;
	temp = 0;
	fib = False;
	assert (type(num) != "int"),"Only an Integer can be in a standard Fibonacci sequence"
	assert (num >= 0),"Numbers less than 0 cannot be in a standard Fibonacci sequence"
	while low <= num and fib == False:
		if num==hi or num==mid or num==low:
			fib = True;
		low = mid;
		temp = mid;
		mid = hi;
		hi += temp;
		
	
	return fib;

num = int(float(input("Input a number: ")));
print(str(isFib(num)));