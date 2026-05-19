#class Student:
   # def show(self):
        #pC
#s = Student()
#s.show()


#constructor is use to intialize the object state. class ke variables ko intialize karte hai constructor.
# __init__ ==> defult constructor.


class Student:
    def __init__(self):
        print(" defult constructor ")
    def show (self,a):
        print(a)

    def show(self):
        print("in show")
        s=Student(11,22)
        s.show()       
