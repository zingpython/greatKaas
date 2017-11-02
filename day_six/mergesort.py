
def mergeSort(unsorted):
	sorted_list = []

	for item in unsorted:
		sorted_list.append( [item] )

	while len(sorted_list) > 1:

		iter_list = []

		for index in range(0, len(sorted_list), 2):

			left = sorted_list[index]
			if index == len(sorted_list)-1:
				right = []
			else:
				right = sorted_list[index+1]

			temp_list = []

			while len(left) > 0 or len(right) > 0:
				if len(left) == 0:
					temp_list.append( right.pop( 0 ) )
				elif len(right) == 0:
					temp_list.append( left.pop( 0 ) )
				elif left[0] <= right[0]:
					temp_list.append( left.pop( 0 ) )
				elif right[0] < left[0]:
					temp_list.append( right.pop( 0 ) )

			iter_list.append( temp_list )
		sorted_list = iter_list

	return sorted_list[0]


print( mergeSort( [28,54,26,17,19,44,50,20] ))