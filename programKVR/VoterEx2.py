#Program for deciding wether the citizen is eligible to Vote or not
#VoterEx2.py
while(True):
	age=int(input("Enter Age of Voter:"))
	if(age>=18) and (age<=100):
		break
	else:
		print("\t{} Years Invalid Age,Try again".format(age))

print("{} Years Voter is Eligible to Vote".format(age))