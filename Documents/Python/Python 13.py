def string_scramble(fir,sec):
	fir = str(fir).lower();
	sec = str(sec).lower();
	check = [];
	for i in range(0,len(fir),1):
		appears = False;
		for j in range(0,len(sec),1):
			if fir[i] == sec[j]:
				appears = True;
		check.append(appears);
	result = True;
	if len(check) > 0:
		for k in range(0, len(check),1):
			if check[k] == False:
				result = False;
	else:
		result = False;
	return result;


#first = str(input("Enter the first string: "));
#second = str(input("Enter the string to compare it to: "));
#print(string_scramble(first, second));