#FactEExWhile1.py
n=int(input("Enter a Number for Cal factorial:"))
if(n<0):
    print("{} is Invalid Input".format(n))
else:
    f=1
    i=1
    while(i<=n):
        f=f*i
        i=i+1
    else:
        print("Factorial({})={}".format(n,f))
