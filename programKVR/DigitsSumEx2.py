#Program for finding sum of digits of a given number
#DigitsSumEx2.py
n=input("Enter a Number:")
if(int(n)<=0):
    print("{} is invalid Input".format(n))
else:
    s=0
    print("Given Number:{} ".format(n))
    digits=n.split()
    for digit in digits[0]:
        s=s+int(digit)
    else:
        print("Sum of Digits={}".format(s))




