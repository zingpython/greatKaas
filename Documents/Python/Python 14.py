def largest_prime(num):
	num = int(float(num));
	largest = 1;
	for i in range(2,num,1):
		if (num%i) == 0:
			prime = True;
			for j in range(2,i,1):
				if (i%j) == 0 and i != j:
					prime = False;
			if prime == True:
				largest = i;
	
	if largest == 1:
		largest = num;
	return largest;

#print(largest_prime(600001));