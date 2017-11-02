limit = int(input("Enter the limit: "))

sieve_list = list( range(2, limit+1) )


#While loop moves from start of list to end of list
#We use a while loop because we will be removing items from the list
index = 0
while index < len(sieve_list):

	#Index2 starts at index +1 because we want to check if every item after the current index is divisible by index
	index2 = index+1

	#While loop will run until out of range of the list
	while index2 < len(sieve_list):
		#If the item at index2 is divisible by the item at index remove the item at index2 and do not increment index2
		if sieve_list[index2]%sieve_list[index] == 0:
			#Removes the item at index2 and by removing it index2 is now pointing to the next item
			sieve_list.pop(index2)
		#If the item at index2 is not divisible by the item at index then we move to the next index2
		else:
			index2 = index2 + 1

	#increasae index to view next item in list
	index = index +1


#output final list
print(sieve_list)