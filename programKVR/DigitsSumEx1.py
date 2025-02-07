#Program for finding sum of digits of a given number
#DigitsSumEx1.py
n=int(input("Enter a Number:"))
if(n<=0):
    print("{} is invalid Input".format(n))
else:
    s=0
    while(n>0):
        r=n%10
        s=s+r
        n=n//10
    else:
        print("Digits Sum={}".format(s))
