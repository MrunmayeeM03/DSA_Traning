class Queue:

    def __init__(self):

        self.queue = []
        self.rear = -1

    # Check Empty
    def isEmpty(self):

        return self.rear == -1

    # Insert Operation
    def insert(self, ele):

        self.queue.append(ele)
        self.rear += 1

        print(ele, "is inserted")

    # Delete Operation
    def delete(self):

        if self.isEmpty():

            print("Queue is Empty")

        else:

            ele = self.queue.pop(0)
            self.rear = self.rear - 1

            print(ele, "is deleted")


# Main Program
obj = Queue()

obj.insert(10)
obj.insert(20)
obj.insert(30)

print("Queue:", obj.queue)

obj.delete()

print("Queue after delete:", obj.queue)