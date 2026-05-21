def add(self,a):
    print(a)
def  add(self,a,b):
    print(a+b)
def  add(a,b,c):
     print(a+b+c)
     #add(11)
     #add(22,33)
     add(11,22,33)    


     #in python overloading is not allowed it only work in java and c++    



     class Parent:
         def __init__(self):
         self.speed=100
         print("cash,gold")

         def bike(self):
             print("splender+",self.speed)

             class Child(Parent):
                 def __init__(self):
                     self.speed=150
                     def bike(self):
                         print("HB",self.speed)
                         obj=Child()
                         obj.bike()
         
    