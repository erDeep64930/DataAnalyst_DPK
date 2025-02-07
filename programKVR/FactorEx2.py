#Program for obtaining Factors of a given number
#FactorEx2.py
n=int(input("Enter a Number for getting its Factors:"))
if(n<=0):
    print("{} is Inavlid Input".format(n))
else:
    print("-"*50)
    print("Factor of {}".format(n))
    print("-" * 50)
    for i in range(1,(n//2)+1):
        if(n%i==0):
            print("\t{}".format(i))
    else:
        print("\t{}".format(n))
        print("-" * 50)
