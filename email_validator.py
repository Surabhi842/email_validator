#Python program to check that entered email is
#valid or not...
def email_validator(email): #defines a function
    #check length,first character and @ count in entered email
    if len(email) >= 6 and email[0].isalpha() and email.count("@")==1: 
        #check for . position and count
        if ((email[-4]==".") or (email[-3]==".")) and email.count(".")==1:
            #loop iterates all characters in email   
            for ch in email:
                if (ch.isalpha() and ch.islower()) or ch.isdigit() or ch=="@" or ch==".":
                    continue
                else:
                    return False
            return True 
        else:
            print("Invalid dot position or dot count")  
            return False     
    else:
        print("Check you length,first character or @ count")            
        return False
#basic format=g@g.in,g@g.com(means atleast contains 6 characters)
email=input("Enter you email:") 
result=email_validator(email)
if result:
    print("Congrats!!! Your email is totally valid..")
else:
    print("Oops!!! Your email is invalid...")



