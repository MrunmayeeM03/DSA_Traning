cp = int(input("Enter cost price: "))
 student = input ("are you a student or not")("y/n")
if student == "yes":

if cp <= 500:
 discount = cp* 0.10
else :
    discount = cp*0.05 

if cp >= 500 :
    discount = cp* 0.08
else : 
   discount = cp*0.02

net= cp- discount 
print ("cost price=",cp)
print ("net price=",netprice)
print ("discount=",dis)