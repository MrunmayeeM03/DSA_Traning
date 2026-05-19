import sys
class GetNode:
    def __init__(self):
        self.data=None
        self .head=None
class LinkList:
    def __init__(self):
         self .head=None
    def append(self):
        data=int(input("enter data:"))
        newNode=GetNode()
        newNode.data=data
        if self.head==None:
            self.head=newNode
        else:
            ptr=self.head
            while ptr.next!=None:
                ptr=ptr.next
                ptr.next=newNode
                print(data,"is added")

        
    def traverse(self):

        if self.head == None:
            print("Linked List is Empty")

        else:
            ptr = self.head

            while ptr != None:
                print(ptr.data, end=" -> ")
                ptr = ptr.next

            print("None")
if __name__ == '__main__':

    obj = LinkList()

    while True:

        print("\n1. Append")
        print("2. Traverse")
        print("0. Exit")

        n = int(input("Select any choice: "))

        if n == 1:
            obj.append()

        elif n == 2:
            obj.traverse()

        elif n == 0:
            sys.exit(0)

        else:
            print("Invalid Choice")    

   
       