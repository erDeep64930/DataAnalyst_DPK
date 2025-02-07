#LineintoWordsEx1.py
line=input("Enter Line of Text:")
print("----------------------------------------")
print("Given Line:{}".format(line))
print("----------------------------------------")
words=line.split() # here words is an obj of list
print('Given Words={}'.format(words))
print("----------------------------------------")
print("\tWords\t\tLength")
print("----------------------------------------")
i=0
while(i<len(words)):
    print("\t{}\t\t{}".format(words[i],len(words[i])))
    i=i+1
else:
    print("----------------------------------------")

