#Program for finding sum of digits of a given number
#DigitsSumEx2.py
n=input("Enter a Number:")
if(int(n)<=0):
    print("{} is invalid Input".format(n))
else:
    s=0
    print("Given Number:{} ".format(n))
    digits=list(n) # Type Casting str into digits
    for digit in digits:
        s=s+float(digit)
    else:
        print("sum of digits={}".format(s))





