#Program for finding Sum of First Natural Numbers
#NatNumsSumEx1.py
n=int(input("Enter How Numbers Sum u want to Find:"))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    print("-"*50)
    print("{} First Natural Numbers Sum".format(n))
    print("-" * 50)
    s=0
    i=1
    while(i<=n):
        print("\t{}".format(i))
        s=s+i
        i=i+1
    else:
        print("-"*50)
        print("Sum={}".format(s))
        print("-" * 50)