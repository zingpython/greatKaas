i = int(input("Triangle Size: "));
for y in range(1,i+1,1):
	for z in range(0,i,1):
		if (z) >= (i-y):
			print("*",end="");
		else:
			print(" ",end="");
	print();
