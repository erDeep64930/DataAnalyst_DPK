#InnerLoopsEx4.py--while loop in for loop
for i in range(5,0,-1): # Outer Loop
    print("value of i outer loop:{}".format(i))
    print("------------------------------")
    j=3
    while(j>0): # Inner Loop
        print("\tvalue of j-Inner Loop:{}".format(j))
        j=j-1
    else:
        print("\tI am coming out of inner loop")
        print("------------------------------")
else:
    print("I am coming out of outer loop")

