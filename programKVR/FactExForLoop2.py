#FactExForLoop2.py
n=int(input("Enter a Number for Cal factorial:"))
if(n<0):
    print("{} is Invalid Input".format(n))
else:
    f=1
    for i in range(n,0,-1):
        f=f*i
    else:
        print("Factorial({})={}".format(n,f))
