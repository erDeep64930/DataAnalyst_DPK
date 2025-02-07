#program for Generating student Marks Report
#StudentMarksReport2.py
#Validation of Student Number
while(True):
	while(True):
		sno=int(input("Enter Student Number:"))
		if(sno>0):
			break
		print("\t{} Is Invalid Student Number:".format(sno))
	#Accept Student Name
	sname=input("Enter Student Name:")
	#Validation of C lang Marks(0-100)
	while(True):
		cm=int(input("Enter Marks in C:"))
		if(cm>=0) and (cm<=100):
			break
		print("\t{} Is Invalid Marks in C:".format(cm))
	#Validation of CPP lang Marks(0-100)
	while(True):
		cppm=int(input("Enter Marks in C++:"))
		if(0<=cppm<=100):
			break
		print("\t{} Is Invalid Marks in C++:".format(cppm))

	#Validation of PYTHON lang Marks(0-100)
	while(True):
		pym=int(input("Enter Marks in PYTHON:"))
		if(0<=pym<=100):
			break
		print("\t{} Is Invalid Marks in PYTHON:".format(pym))
	#Compute TotalMarks and Percentage
	totmarks=cm+cppm+pym
	percent=(totmarks/300)*100
	#Decide the grade
	if(cm<40)  or  (cppm<40) or (pym<40):
		grade="FAIL"
	else:
		if(totmarks>=250) and (totmarks<=300):
			grade="DISTINCTION"
		elif(totmarks>=200) and (totmarks<=249):
			grade="FIRTST"
		elif(totmarks>=150) and (totmarks<=199):
			grade="SECOND"
		elif(totmarks>=120) and (totmarks<=149):
			grade="THIRD"
	#Display Student Marks Report
	print("="*50)
	print("\t\tStudent Marks Report:")
	print("="*50)
	print("\tStudent Number:{}".format(sno))
	print("\tStudent Name:{}".format(sname))
	print("\tStudent Marks in C:{}".format(cm))
	print("\tStudent Marks in C++:{}".format(cppm))
	print("\tStudent Marks in PYTHON:{}".format(pym))
	print("-"*50)
	print("\tStudent Total Marks:{}".format(totmarks))
	print("\tStudent Percentage of Marks:{}".format(percent))
	print("\tStudent Grade:{}".format(grade))
	print("="*50)
	ch=input("\nDo u want to Enter Another Student Data(yes/no):")
	if(ch.lower()=="no"):
		print("Thx for using Program")
		break






