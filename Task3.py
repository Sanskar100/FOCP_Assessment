import random
def random_string(Ans): 
    """choosing a random string from a list of strings"""
    return random.choice(Ans)

def email_valadiation(email,domain): 
    """valaditing given email"""
    if email.count("@")<0 and email.count("@")>2:
        return False
    
    elif len(email[:email.find("@")])<2:
        return False
    elif email[email.find("@"):]!=domain:
        return False
    else:
        return True

def get_names(email): 
    """ returns a name from a given email address """
    names=email[:email.find("@")]
    return names

def spotting(wo,se): 
    """checking if a string is a substring"""
    if wo.lower() in se.lower(): 
        return True


def setup():
        print("Welcome to pop chat\n""One of our operators will be pleased to help you today.")
        ls_operator=["James","Nike","Harry","Josh"] # random names of the operators
        ls_reply=["Hmmm","Oh, yes,I see","Tell me more","Please say once again"] # random reply from the operators
        ls_exit=["Bye","exit","Have a great day"] 
        email=input("Please enter your Poppleton email address: ") # asking the user to input their University email address
        if email_valadiation(email,"@pop.ac.uk"): # checking if the email in valid or not
            print("Hi,{}!Thank you, and Welcome to PopChat!\n""My name is {},and it will be my pleasure to help you.".format(get_names(email),random_string(ls_operator)))
            while True:
                userinput=input("How can I help you?: ") # asking the to enter their problem
                if random.randint(1,10)>9: # ramdomly choosing number between 1 to 10, checking if is greater than 9
                    print("Network error")
                    break
                for i in ls_exit:
                    if spotting(i,userinput): 
                        return
                if spotting("library",userinput):
                    print("The library is closed today.")
                elif spotting("WiFi",userinput):
                    print("WiFi is excellent across the campus.")
                elif spotting("deadline",userinput):
                    print("Your deadline has been extended by two working days.")
                elif spotting("Science lab",userinput):
                    print("Our lab are well equiped.")
                elif spotting("teachers",userinput):
                    print("We have highly qualified teachers.")
                elif spotting("activities",userinput):
                    print("There are many activities you can do in the campus like playing basketball.")
                else:
                   print (random_string(ls_reply))
                
setup()


    



        