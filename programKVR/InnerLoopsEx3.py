#InnerLoopsEx2.py--for loop in while loop
i=1
while(i<=5): #Outer Loop
    print("value of i outer loop:{}".format(i))
    print("------------------------------")
    for j in range(3,0,-1): # inner loop
        print("\tvalue of j-Inner Loop:{}".format(j))
    else:
        i=i+1
        print("\tI am coming out of inner loop")
        print("------------------------------")
else:
    print("I am coming out of outer loop")