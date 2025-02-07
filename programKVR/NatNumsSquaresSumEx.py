#Program for finding Sum of Squares of First Natural Numbers
#NatNumsSquaresSumEx.py
n=int(input("Enter How Numbers Sum u want to Find:"))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    print("-"*50)
    print("\tNatNums\tSquares\tCubes")
    print("-" * 50)
    s,ss,cs=0,0,0
    i=1
    while(i<=n):
        print("\t{}\t\t{}\t\t{}".format(i,i**2,i**3))
        s=s+i
        ss = ss + i ** 2
        cs=cs+i**3
        i=i+1

    else:
        print("-" * 50)
        print("\t{}\t\t{}\t\t{}".format(s,ss,cs))
        print("-" * 50)
