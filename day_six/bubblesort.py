def bubbleSort(unsorted):
	swapped = True
	while swapped == True:
		print(unsorted)
		swapped = False
		for index in range( len(unsorted) ):
			if index != len(unsorted)-1:
				if unsorted[index+1] < unsorted[index]:
					temp = unsorted[index]
					unsorted[index] = unsorted[index+1]
					unsorted[index+1] = temp
					swapped = True

	return unsorted


print(bubbleSort([47,98,3,9,25,13,12,38,45]))