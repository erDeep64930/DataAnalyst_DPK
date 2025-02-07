#FactEExWhile2.py
n=int(input("Enter a Number for Cal factorial:"))
if(n<0):
    print("{} is Invalid Input".format(n))
else:
    f=1
    i=n
    while(i>0):
        f=f*i
        i=i-1
    else:
        print("Factorial({})={}".format(n,f))
