class Stacks:

    def __init__(self):
        self.stack = []
        self.top = -1

    # Push Operation
    def push(self, ele):

        self.stack.append(ele)
        self.top = self.top + 1

        print(ele, "is pushed")

    # Traverse Stack
    def traverse(self):

        if self.isEmpty():
            print("Stack is empty")

        else:
            print("Stack elements are:")

            for i in range(self.top, -1, -1):
                print(self.stack[i])

    # Check Empty
    def isEmpty(self):

        if self.top == -1:
            return True

        else:
            return False

    # Pop Operation
    def pop(self):

        if self.isEmpty():
            print("Stack is empty")

        else:
            ele = self.stack[self.top]
            self.stack.pop()
            self.top -= 1

            return ele

    # Peek Operation
    def peek(self):

        if self.isEmpty():
            print("Stack is empty")

        else:
            print("Top element is:", self.stack[self.top])


if __name__ == '__main__':

    obj = Stacks()

    while True:

        print("\n1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Traverse")
        print("0. Exit")

        ch = int(input("Select any choice: "))

        if ch == 1:

            ele = int(input("Enter data: "))
            obj.push(ele)

        elif ch == 2:

            ele = obj.pop()

            if ele is not None:
                print(ele, "is popped")

        elif ch == 3:

            obj.peek()

        elif ch == 4:

            obj.traverse()

        elif ch == 0:

            print("Program Ended")
            break

        else:

            print("Invalid Choice")