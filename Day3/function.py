#function is a self contain block which is design and excuted seperatly and return o/p to main function

# main function in python ____  if_name_=='__main__':  not complusory to add main function


def add():
    a=int(input("enter a: "))
    b=int(input("enter b: "))
    res=a+b
    print("Addition is",res)
if __name__ == "__main__":
    add()

