i = int(input("How far do we multiply? "));
for y in range(1,i+1,1):
	for z in range(1,i+1,1):
		print(str(y*z),end="");
		if (y*z)>=10:
			print("| ",end="");
		else:
			print(" | ",end="");
	print();