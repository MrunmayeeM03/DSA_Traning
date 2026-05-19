# import sys
# class Queue:
#     def __init__(self):
#       self.queue=[]
#       self.rear=-1
#       self.front=0
#       self.capacity=5

#       def isfull(self):
#         if self.top==self.capacity-1:
#            return True
#         else:
#             return False
#         def insert(self,ele):
#             pass
#         def traverse(self):
#             pass
#         def isEmpty(self):
#             if self.rear==-1:
#                 return True
#             else:
#                  print("False")


# if __name__ == '__main__':
   
                
#    while True:
#         obj=Queue()

#         print("\n1. insert")
#         print("2. delete" )
#         print("3. Peek")
#         print("4. Traverse")
#         print("0. Exit")

#         ch = int(input("Enter choice: "))

#         if ch == 1:

#             ele = int(input("Enter data: "))
#             obj.insert(ele)
#         elif ch==2:
#              obj.delete()
#         elif ch==3:
#              obj.peek()
#         elif ch==4:
#             obj.traverse()
#         elif ch==0:
#             sys.exit(0)       




# import sys

# class Queue:

#     def __init__(self):

#         self.queue = []
#         self.front = 0
#         self.rear = -1
#         self.capacity = 5

#     # Check Full
#     def isfull(self):

#         return self.rear == self.capacity - 1

#     # Check Empty
#     def isEmpty(self):

#         return self.rear == -1

#     # Insert Operation
#     def insert(self, ele):

#         if self.isfull():

#             print("Queue is Full")

#         else:

#             self.rear += 1
#             self.queue.append(ele)

#             print(ele, "is inserted")

#     # Delete Operation
#     def delete(self):

#         if self.isEmpty():

#             print("Queue is Empty")

#         else:

#             ele = self.queue.pop(0)
#             self.rear -= 1

#             print(ele, "is deleted")

#     # Peek Operation
#     def peek(self):

#         if self.isEmpty():

#             print("Queue is Empty")

#         else:

#             print("Front element is:", self.queue[0])

#     # Traverse Operation
#     def traverse(self):

#         if self.isEmpty():

#             print("Queue is Empty")

#         else:

#             print("Queue Elements:")

#             for i in self.queue:
#                 print(i)


# if __name__ == '__main__':

#     obj = Queue()

#     while True:

#         print("\n1. Insert")
#         print("2. Delete")
#         print("3. Peek")
#         print("4. Traverse")
#         print("0. Exit")

#         ch = int(input("Enter choice: "))

#         if ch == 1:

#             ele = int(input("Enter data: "))
#             obj.insert(ele)

#         elif ch == 2:

#             obj.delete()

#         elif ch == 3:

#             obj.peek()

#         elif ch == 4:

#             obj.traverse()

#         elif ch == 0:

#             sys.exit(0)

#         else:

#             print("Invalid Choice")



  
import sys
class Queue:
    def _init_(self):
        self.queue=[]
        self.rear=-1
        self.front=0
        self.CAPACITY=5

    def isFull(self):
        if self.rear==self.CAPACITY-1:
            return True
        else:
            return False

    def insert(self,ele):
        if self.isFull():
            print("Queue is full")
        else:
            self.queue.append(ele)
            self.rear+=1

    def traverse(self):
        if not self.isEmpty():
            print("Queue elements:")
            for i in range(self.front, self.rear+1):
                print(self.queue[i], end=" ")
            print()
        else:
            print("Queue is empty")

    def isEmpty(self):
        if self.rear==-1:
            return True
        else:
            return False

    def delete(self):
      pass
    
    def peek(self):
        if not self.isEmpty():
            print("Front element:", self.queue[self.front])
        else:
            print("Queue is empty")

if __name__ == '_main_':
    obj=Queue()
    while True:
        print("1. Insert")
        print("2. Delete")
        print("3. Peek")
        print("4. Traverse")
        print("0. Exit")
        ch=int(input("Select any choice :"))
        if ch==1:
            ele=int(input("Enter data: "))
            obj.insert(ele)
        elif ch==2:
            obj.delete()
        elif ch==3:
            obj.peek()
        elif ch==4:
            obj.traverse()
        elif ch==0:
            sys.exit(0)






