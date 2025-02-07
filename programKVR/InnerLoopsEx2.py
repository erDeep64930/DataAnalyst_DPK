#InnerLoopsEx2.py--while loop in while loop
i=1
while(i<=5): #Outer Loop
    print("value of i outer loop:{}".format(i))
    print("------------------------------")
    j=1
    while(j<=3): # Inner Loop
        print("\tvalue of j-Inner Loop:{}".format(j))
        j=j+1
    else:
        i=i+1
        print("\tI am coming out of inner loop")
        print("------------------------------")
else:
    print("I am coming out of outer loop")

