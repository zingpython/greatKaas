#Pseudo Code
#Start function and input target number
#Create empty array
#For i from 2 to target number
	#array[i-2] = i
# i = 0
#while i is less than length of array
	#for j from target num-2 to i subtracting 1 from j each iteration
		#if (array[j] remainder of array[i]) equals 0
			#delete array[j]
	#i++
#return array

def sieve(num):
	num = int(float(num));
	rang = [];
	for i in range(2,num,1):
		rang.append(i);
	j = 0;
	while (j < len(rang)):
		for k in range(len(rang)-1,0,-1):
			if (rang[k] % rang[j]) == 0 and rang[k] != rang[j]:
				del rang[k];
		j+=1;
	return rang;

# print(sieve(121));