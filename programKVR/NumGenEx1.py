#Program for generating 1 to 1 n numbers where n is +ve
#NumGenEx1.py
n=int(input("Enter How Many Numbers u want to generate:"))
if(n<=0):
    print("{} is invalid input".format(n))
else:
    i=1 # Initlization
    while(i<=n): # test Cond
        print("\t{}".format(i))
        i=i+1 # Updation
    print("Program execution completed")
