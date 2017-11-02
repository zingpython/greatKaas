def isOdd(number):
	if number%2 == 1:
		#Number is odd
		return True
	else:
		#Number is even
		return False


def isPalindrome(word):

	first_half = word[0: len(word)//2 ]

	if isOdd( len(word) ):
		second_half = word[-1: (len(word)//2) : -1  ]
	else:
		second_half = word[-1: (len(word)//2)-1 : -1  ]


	if first_half == second_half:
		return True
	else:
		return False

	# print(first_half)
	# print(second_half)

print( isPalindrome("civic") )