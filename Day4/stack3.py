class Stack:

    def __init__(self):
        self.stack = []

    # Push Operation
    def push(self, ele):

        self.stack.append(ele)

        print(ele, "is pushed")

    # Pop Operation
    def pop(self):

        if self.isEmpty():
            print("Stack is empty")

        else:
            ele = self.stack.pop()

            print(ele, "is popped")

    # Peek Operation
    def peek(self):

        if self.isEmpty():
            print("Stack is empty")

        else:
            print("Top element is:", self.stack[-1])

    # Traverse Stack
    def traverse(self):

        if self.isEmpty():
            print("Stack is empty")

        else:
            print("Stack elements are:")

            for i in range(len(self.stack) - 1, -1, -1):
                print(self.stack[i])

    # Check Empty
    def isEmpty(self):

        return len(self.stack) == 0


if __name__ == '__main__':

    obj = Stack()

    while True:

        print("\n1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Traverse")
        print("0. Exit")

        ch = int(input("Enter choice: "))

        if ch == 1:

            ele = int(input("Enter data: "))
            obj.push(ele)

        elif ch == 2:

            obj.pop()

        elif ch == 3:

            obj.peek()

        elif ch == 4:

            obj.traverse()

        elif ch == 0:

            print("Program Ended")
            break

        else:

            print("Invalid Choice")