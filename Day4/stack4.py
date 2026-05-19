#Reverse the arry using stack
import sys
class Stacks:
    def __init__(self):
      self.stack=[]
      self.top=-1
      self.capacity=5

    def isfull(self):
        if self.top==self.capacity-1:
           return True
        else:
            return False
    def push(self,ele):
        if self.isfull():
            print("Stack is full")
        else:
            self.top=self.top+1
            self.stack.append(ele)
            print(ele,"is pushed")
    def traverse(self):
        for i in range(self.top,-1,-1):
            print(self.stack[i])


    arr = [10, 20, 30, 40, 50]

obj = Stacks()

# Push array elements into stack
for i in arr:
    obj.push(i)

# Pop elements back into array
for i in range(len(ar)):
    ar[i] = obj.pop()

print("Reversed Array:", )
