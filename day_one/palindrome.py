word = input("Enter a word: ")

# if word == "".join(reversed(word)):
# 	print("Palindrome")
# 
# if word == word[::-1]:
# 	print("Palindrome")


isPalindrome = True

for x in range( len(word) ):
	if word[x] != word[-x-1]:
		isPalindrome = False

print(isPalindrome)