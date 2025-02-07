#InnerLoopsEx1.py--for loop in for loop
for i in range(1,6): # Outer Loop
    print("value of i outer loop:{}".format(i))
    print("------------------------------")
    for j in range(1,4): # Inner Loop
        print("\tvalue of j-Inner Loop:{}".format(j))
    else:
        print("\tI am coming out of inner loop")
        print("------------------------------")
else:
    print("I am coming out of outer loop")


