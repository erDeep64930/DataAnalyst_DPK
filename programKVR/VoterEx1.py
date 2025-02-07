#Program for deciding wether the citizen is eligible to Vote or not
#VoterEx1.py
age=int(input("Enter Age:"))
if(age>=18):
    print("{} Years Citizen is Eligible to Vote:".format(age))
else:
    print("{} Years Citizen is NOT Eligible to Vote:".format(age))