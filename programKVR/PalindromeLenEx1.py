#Program for finding Largest Palindrome from list of words
#PalindromeLenEx1.py
lst=["MOM","DAD","RACECAR","NAN","MALAYALAM","MADAM","LIRIL"]
d=dict() # create an empty dict
for word in lst:
	d[word]=len(word)
else:
	print("-----------------------------------------")
	for pname,plen in d.items():
		print("\t{}--->{}".format(pname,plen))
	else:
		plist=[] #empty list for adding Largest Palindrome name
		print("-----------------------------------------")
		#Logic for finding Largest palindrome
		mpl=max(d.values())  # 9
		for dw,dwlen in d.items():  
			if(dwlen==mpl):
				plist.append(dw)
		else:
			print("Largest Palindrome:",end=" ")
			for val in plist:
				print(val)

		