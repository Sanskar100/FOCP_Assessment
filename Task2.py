from statistics import mean

list1=[]
while True:
    speed=input("Enter a speed: ") #ask to input the speed 
    if speed=="":
        break
    
    Miles=float(speed[1:])
    if speed[0]=="U":
        list1.append(Miles)
    else: 
        Miles=Miles*0.621371 # converting miles into kilometer
        list1.append(Miles)

if list1!=[]: #checking if the input list is empty or not 
    Maximum=max(list1) #maximum value holding in the list
    Minimum=min(list1) #minimum value holding in the list
    average=mean(list1) #average value holding in the list
    print("Number of entered data",len(list1))
    print("Maximum speed: {}, {}".format (Maximum,Maximum/0.621371))
    print("Minimum speed: {},{}".format (Minimum,Minimum/0.621371))  
    print("Average speed: {}, {}".format (average,average/0.621371))

else:
    print("No values entered, No thing to do")




    