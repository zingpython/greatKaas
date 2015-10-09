def Fact(num):
	assert(type(num)!="int"), "Argument must be an integer to proceed"
	if num <= 1:
		return 1;
	else:
		return (num * Fact(num-1));


import sys;
print(Fact(int(float(sys.argv[1]))));
