#Program for finding product First Natural Numbers
#ProductNumberEx1.py
n=int(input("Enter How Numbers Product u want to Find:"))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    print("-"*50)
    print("Product of First {} Natural Nums:".format(n))
    print("-" * 50)
    p=1
    i=1
    while(i<=n):
        print("\t{}".format(i))
        p=p*i
        i=i+1
    else:
        print("-" * 50)
        print("Product={}".format(p))
        print("-" * 50)