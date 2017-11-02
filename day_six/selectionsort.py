def selectionSort(unsorted):
	sorted_list = []

	while len(unsorted) > 0:

		lowest_index = 0

		for item in range(len(unsorted)):
			if unsorted[lowest_index] > unsorted[item]:
				lowest_index = item

		sorted_list.append( unsorted.pop(lowest_index) )

	return sorted_list


print(selectionSort([6,12,2,35,79,16,45,38,47,25]))