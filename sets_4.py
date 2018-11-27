#sets_4.py JM
alpha = {"a","b","c","d","e","f"}
bravo = {"z","y","x","w","v"}
charlie = alpha.union(bravo)
charlie.update("g","h","i","j","k")
for x in charlie:
	print(x," ",end="")
print()
#pop all the records
for i in range(len(charlie)):
	print("pop ", i," ",end="")
	thepop = charlie.pop()
	print (thepop)
	
"""
The union method combines two sets and updates itself.
notices the udpate function. Notice the update funtion.
You can not pop from an empty setself.
The concept of "pop" is an important
function in data structers that resemble.
"""
