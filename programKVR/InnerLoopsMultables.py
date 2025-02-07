#InnerLoopsMultables.py
n=int(input("How Many Mul tables u want:"))
if(n<=0):
    print("{} is Invalid Input:".format(n))
else:
    for num in range(1,n+1): # Outer Loop--Supply Number
        print("------------------------------")
        print("Mul Table for {}".format(num))
        print("------------------------------")
        for i in range(1,11): # Inner Loop--displays Mul table
            print("\t{} x {}={}".format(num,i,num*i))
        else:
            print("------------------------------")