#Program for generating n to 1 numbers where n is +ve
#NumGenEx2.py
n=int(input("Enter How Numbers u want to generate:"))
if(n<=0):
    print("{} is Invalid input".format(n))
else:
    i=n # Initlization Part
    while(i>0):
        print("\t{}".format(i))
        i=i-1
    else:
        print("I am from else part of while loop")
    print("Program Execution Completed")
