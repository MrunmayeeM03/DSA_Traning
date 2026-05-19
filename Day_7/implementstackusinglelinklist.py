

import sys
class GetNode:

    def __init__(self):
        self.data = None
        self.next = None

class Stack:

    def __init__(self):
        self.top = None

   
    def push(self):

        data = int(input("Enter data: "))

        newNode = GetNode()
        newNode.data = data

        
        newNode.next = self.top
        self.top = newNode

        print(data, "is pushed into stack")

   
    def pop(self):

        if self.top is None:
            print("Stack Underflow")

        else:
            temp = self.top
            self.top = self.top.next

            print(temp.data, "is popped")

   
    def peek(self):

        if self.top is None:
            print("Stack is Empty")

        else:
            print("Top Element:", self.top.data)

    
    def display(self):

        if self.top is None:
            print("Stack is Empty")

        else:
            ptr = self.top

            while ptr is not None:
                print(ptr.data, end=" -> ")
                ptr = ptr.next

            print("None")



if __name__ == '__main__':

    obj = Stack()        

    while True:

        print("\n1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display")
        print("0. Exit")

        n = int(input("Select any choice: "))

        if n == 1:
            obj.push()

        elif n == 2:
            obj.pop()

        elif n == 3:
            obj.peek()

        elif n == 4:
            obj.display()

        elif n == 0:
            sys.exit(0)

        else:
            print("Invalid Choice")