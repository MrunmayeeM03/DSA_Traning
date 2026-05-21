#  Single level


# class A:
#     def showA(self):
#          print("i am in class A")
# class B(A):
#      def showB(self):
#           print("I am in class B")

# if __name__ =='__main__':
#      obj=B()
#      obj.showA()
#      obj.showB()






# #multi level
# class A:
#     def showA(self):
#           print("i am in class A")
# # class B(A):
# #      def showB(self):
# #           print("I am in class B")
# class C(B):
#      def showB(self):
# #           print("I am in class C")
# if __name__ =='__main__':
# #      obj=B()
# #      obj.showA()
# #      obj.showB()
#        obj.showC()



#Hybrid Inheritance
# class A:
#     def showA(self):
#         print("Class A")


# class B(A):
#     def showB(self):
#         print("Class B")


# class C(A):
#     def showC(self):
#         print("Class C")


# class D(B, C):
#     def showD(self):
#         print("Class D")


# obj = D()

# obj.showA()
# obj.showB()
# obj.showC()
# obj.showD()




#multi level
# class A:
#     def showA(self):
#         print("Class A")


# class B(A):
#     def showB(self):
#         print("Class B")


# class C(B):
#     def showC(self):
#         print("Class C")


# obj = C()

# obj.showA()
# obj.showB()
# obj.showC()