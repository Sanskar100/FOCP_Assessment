print(" Stop! Who would cross the Bridge of Death \n Must answer me these questions three, 'ere the other side he see.")

flag=False
name=input("What is your name?")
if "arthur" not in name.lower(): # checking if  the name arthur 
    seek=input("what you seek?")
    
    if "grail" in seek.lower(): #checking if the user says grail
        colour=input("What is your favourite colour?")
        
        if colour[0].lower()!=name[0].lower():
            flag=True
    else:
        flag=True        
if flag:
    print("You are not allowed")
else:
    print("You are allowed")



