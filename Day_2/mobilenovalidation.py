mob = input("enter mob number:")
if mob.isdigit():
    if len(mob)==10:
        if mob[0]=='6' or mob[0]== '7' or mob[0]=='8' or mob[0]=='9':
            print ("valid number")
        else:
            print ("invalid")
        
    else:    
         print("mobile no must be of 10 digit")
         
else:
     print ("only digits are allowed")       


