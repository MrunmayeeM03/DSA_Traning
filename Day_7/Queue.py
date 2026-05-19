#implement Queue using linked List
#FIFO
 #append()->  insert()
#deleteBegin()->delete()
#traverse()
#front=head
#rear=newNode


class Node:
    def __init__(self,data):
     self.data=data
     self.next=None

class Queue:
    def __init__(self,data):
       self.front=None
       self.rear=None
       # insert / append
    def insert(self, data):
        newNode = Node(data)


        if self.front is None:
            self.front = newNode
            self.rear = newNode
        else:
            self.rear.next = newNode
            self.rear = newNode


    # delete from beginning
    def delete(self):
        if self.front is None:
            print("Queue is Empty")
            return

        temp = self.front
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        print(temp.data, "deleted from queue")

    # traverse queue
    def traverse(self):
        if self.front is None:
            print("Queue is Empty")
            return

        temp = self.front

        print("Queue Elements:")
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next
        print()


# Driver Code
q = Queue()

q.insert(10)
q.insert(20)
q.insert(30)

q.traverse()

q.delete()

q.traverse()

