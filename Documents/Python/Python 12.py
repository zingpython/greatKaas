import sys;

def palindrome(newstr):
	pal = list(str(newstr).lower().replace(" ",""));
	for i in range(len(pal)-1,0,-1):
		if pal[i].isalpha() != True:
			del pal[i];
	assert(len(pal) != 0),"A palindrome must have alpha numeric characters in it."

	isPal = True;
	for i in range(0,len(pal),1):
		if pal[i] != pal[len(pal)-(i+1)]:
			isPal = False;
	
	return isPal;

print(palindrome(sys.argv[1]));