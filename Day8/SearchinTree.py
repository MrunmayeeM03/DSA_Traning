def search(self, key):
    if self.data == key:
        print("Node found")
        return

    if key < self.data:
        if self.leftchild:
            self.leftchild.search(key)
        else:
            print("Node not found")

    else:
        if self.rightchild:
            self.rightchild.search(key)
        else:
            print("Node not found")















            