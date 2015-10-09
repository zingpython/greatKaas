import sys;

temparray = [];
for j in range(1,len(sys.argv),1):
	temparray.append(sys.argv[j]);
stack = [];

for i in range(0,len(temparray),1):
	if temparray[i] == "-" or temparray[i] == "+" or temparray[i] == "*" or temparray[i] == "/":
		sec = int(stack.pop());
		fir = int(stack.pop());
		if temparray[i] == "-":
			stack.append(fir-sec);
		elif temparray[i] == "+":
			stack.append(fir+sec);
		elif temparray[i] == "*":
			stack.append(fir*sec);
		elif temparray[i] == "/":
			stack.append(fir/sec);
	else:
		stack.append(temparray[i]);

print(str(stack[0]));