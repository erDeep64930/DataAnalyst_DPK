#Innerrandmonmultables.py
n=int(input("How Many Mul tables u want:"))
if(n<=0):
    print("{} is Invalid Input:".format(n))
else:
    lst=list()
    for i in range(1,n+1):
        val=int(input("Enter {} Number:".format(i)))
        lst.append(val)
    else:
        print("-"*50)
        print("Given List of Values:{}".format(lst))#[12, 19, 9, -5, 0]
        print("-" * 50)
        for num in lst: # Outer Loop--supply the value from list obj
            if(num<=0):
                print("{} invalid input".format(num))
            else:
                print("-" * 50)
                print("Mul table for {}".format(num))
                print("-" * 50)
                for i in range(1,11):#Inner loop-- display Mul table
                    print("\t{} x {}={}".format(num,i,num*i))
                else:
                    print("-" * 50)



