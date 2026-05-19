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
         
    
if __name__ == '__main__':
    obj=Stacks() 
    while True:
        print("1.Push") 
        print("2.Pop") 
        print("3.peek") 
        print("4.traverse")
        print("0.Exit") 
        ch=int(input("select any choice"))
        if ch==1:
            ele=int(input("enter data:"))
            obj.push(ele)
        elif ch==2:
            obj.pop()
        elif ch==3:
            obj.peek()
        elif ch==4: