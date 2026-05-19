# Reverse Queue Using Stack

# import sys

# class Stacks:

#     def __init__(self):

#         self.stack = []
#         self.top = -1
#         self.capacity = 5

#     def isfull(self):

#         return self.top == self.capacity - 1

#     def push(self, ele):

#         if self.isfull():

#             print("Stack is full")

#         else:

#             self.top += 1
#             self.stack.append(ele)

#     def pop(self):

#         if self.top == -1:

#             print("Stack is empty")

#         else:

#             ele = self.stack[self.top]

#             self.stack.pop()
#             self.top -= 1

#             return ele

#     def traverse(self):

#         for i in range(self.top, -1, -1):
#             print(self.stack[i])


# class Queue:

#     def __init__(self):

#         self.queue = []
#         self.rear = -1
#         self.front = 0
#         self.CAPACITY = 5

#     def isFull(self):

#         return self.rear == self.CAPACITY - 1

#     def insert(self, ele):

#         if self.isFull():

#             print("Queue is full")

#         else:

#             self.queue.append(ele)
#             self.rear += 1

#     def traverse(self):

#         if not self.isEmpty():

#             print("Queue elements:")

#             for i in range(self.front, self.rear + 1):
#                 print(self.queue[i], end=" ")

#             print()

#         else:

#             print("Queue is empty")

#     def isEmpty(self):

#         return self.rear == -1

#     def delete(self):

#         if self.isEmpty():

#             print("Queue is empty")

#         else:

#             ele = self.queue.pop(0)
#             self.rear -= 1

#             return ele

#     def peek(self):

#         if not self.isEmpty():

#             print("Front element:", self.queue[self.front])

#         else:

#             print("Queue is empty")


# if __name__ == '__main__':

#     obj1 = Queue()
#     obj = Stacks()

#     # Insert elements into Queue
#     for i in range(obj1.CAPACITY):

#         ele = int(input("Enter element: "))
#         obj1.insert(ele)

#     print("\nOriginal Queue:")
#     obj1.traverse()

#     # Queue -> Stack
#     while not obj1.isEmpty():

#         ele = obj1.delete()
#         obj.push(ele)

#     # Stack -> Queue
#     while obj.top != -1:

#         ele = obj.pop()
#         obj1.insert(ele)

#     print("\nReversed Queue:")
#     obj1.traverse()


# Reverse Queue Using Stack with Menu Driven Program

import sys


class Stacks:

    def __init__(self):

        self.stack = []
        self.top = -1
        self.capacity = 5

    # Check Stack Full
    def isfull(self):

        return self.top == self.capacity - 1

    # Push into Stack
    def push(self, ele):

        if self.isfull():

            print("Stack is full")

        else:

            self.top += 1
            self.stack.append(ele)

            print(ele, "pushed into stack")

    # Pop from Stack
    def pop(self):

        if self.top == -1:

            print("Stack is empty")

        else:

            ele = self.stack[self.top]

            self.stack.pop()
            self.top -= 1

            return ele


class Queue:

    def __init__(self):

        self.queue = []
        self.front = 0
        self.rear = -1
        self.capacity = 5

    # Check Queue Full
    def isFull(self):

        return self.rear == self.capacity - 1

    # Check Queue Empty
    def isEmpty(self):

        return self.rear == -1

    # Insert into Queue
    def insert(self, ele):

        if self.isFull():

            print("Queue is full")

        else:

            self.queue.append(ele)
            self.rear += 1

            print(ele, "inserted into queue")

    # Delete from Queue
    def delete(self):

        if self.isEmpty():

            print("Queue is empty")

        else:

            ele = self.queue.pop(0)
            self.rear -= 1

            return ele

    # Traverse Queue
    def traverse(self):

        if self.isEmpty():

            print("Queue is empty")

        else:

            print("Queue elements:")

            for i in self.queue:
                print(i, end=" ")

            print()


# Main Program

if __name__ == '__main__':

    q = Queue()
    s = Stacks()

    while True:

        print("\n1. Insert into Queue")
        print("2. Delete from Queue and Push into Stack")
        print("3. Pop from Stack and Insert into Queue")
        print("4. Traverse Queue")
        print("0. Exit")

        ch = int(input("Enter choice: "))

        # Insert into Queue
        if ch == 1:

            ele = int(input("Enter element: "))
            q.insert(ele)

        # Delete from Queue -> Push into Stack
        elif ch == 2:

            ele = q.delete()

            if ele is not None:

                s.push(ele)

                print(ele, "deleted from queue and pushed into stack")

        # Pop from Stack -> Insert into Queue
        elif ch == 3:

            ele = s.pop()

            if ele is not None:

                q.insert(ele)

                print(ele, "popped from stack and inserted into queue")

        # Traverse Queue
        elif ch == 4:

            q.traverse()

        # Exit
        elif ch == 0:

            print("Program Ended")
            sys.exit(0)

        else:

            print("Invalid Choice")