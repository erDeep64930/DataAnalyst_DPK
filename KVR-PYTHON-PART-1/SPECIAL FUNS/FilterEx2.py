#Program for Accepting List Values and Filter Only Numerical Integer Values.
#FilterEx2.py
getintvalues=lambda value: True if(value[0]=="-") and (value[1:].isdigit()) else True if value.isdigit() else False
#Main Program
print("Enter List of Values separated by space:")
lst=[val for val in input().split()]
print("Content of lst=",lst)
vals=tuple(filter(getintvalues,lst))
print("List of Integers=",vals)