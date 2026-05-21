import sys
class BST:
  def __init__(self,key):
        self.leftChild=None
        self.rightchcild=None

  def insetr(self,key):
        if self.data==None:
           self.data=key
           return
        else:
             if key<self.data:
                  if self.leftChild:
                     self.leftChild.insert(key)  
                  else:
                       self.leftChild=BST(key)
             elif key>self.data:
                  if self.rightChild:
                       self.rightChild.insert(key)
                  else:
                       self.rightChild=BST(key)
        
  def perorder(self):
        pass
  def postorder(self):
        pass
  def inorder(self):
        pass
if __name__ =='__main__':
        root= BST()
        while True:
            print("1.Insert")
            print("2.Preorder")
            print("3.postorde")
            print("4.Inorder")
            print("5.Exit")
            n=int(input("Select any choice:"))
        arr=[36,26,46,21,31,11,24,41,56,51,66]    
        if i in range(len(arr)):
              root.insert(arr[i])
        elif n==2:
              root.preorder()
        elif n==3:
              root.inorder()
        elif n==0:
              next.exit()           


