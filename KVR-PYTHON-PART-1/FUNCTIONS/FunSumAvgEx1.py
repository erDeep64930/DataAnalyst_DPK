#Program for finding Sum and Avg for List of Numbers
#FunSumAvgEx1.py
def  acceptvalues():
    n=int(input("Enter How Many Values Sum and Average u want to Find:"))
    if(n<=0):
        return [] # Returning empty list  OR return list()
    else:
        lst=list() # Create empty list for storing list of values
        for i in range(1,n+1):
            value=float(input("Enter {} Value:".format(i)))
            lst.append(value)
        return lst # Here we returning Non-Empty List

def findsumvg(lst): # lst=[10.0, 2.3, 5.6, 7.8, 12.0]
    s=0
    for val in lst:
        s+=val
    else:
        print("--------------------------")
        print("Sum={}".format(s))
        print("Average={}".format(s/len(lst)))
        print("--------------------------")

#Main program
lst=acceptvalues() # Function Call
if(len(lst)==0):
    print("U can't Find sum and Avg bcoz list is empty")
else:
    findsumvg(lst) # function call

