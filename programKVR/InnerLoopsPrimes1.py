#InnerLoopsPrimes1.py
n=int(input("Enter the Range of Prime Numbers:"))
if(n<=1):
    print("{} is Invalid".format(n))
else:
    lst=list()
    for num in range(2,n+1):
        res=False
        for i in range(2,num):
            if(num%i==0):
                res=True
                break # From inner Loop
        if(res==False):
            lst.append(num) # placing primes in list
    else:
        print("List of Primes")
        for v in lst:
            print("\t{}".format(v))


