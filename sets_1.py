#sets_1.py JM
alpha = {"a", "bb", "ccc", "dddd","eeeee","ffffff"}
for x in alpha:
	#print(alpha[x]) #uncomment this line and try 
	print (x)
	print(sorted(alpha))

"""
Look at what is going on here.
A set can not be indexed.
for x in alpha looks at all the elements in
the set and assigns one at a time to the x
varible.
"""
