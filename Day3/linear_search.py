def linear_search(n, arr, target):
    for i in range(n):

        if arr[i] == target:
            print("Element found at index ", i)
            return
    
        print("Element not found")

    
if __name__ == '__main__':
    n= int(input("enter size:"))
    arr=[]
    for i in range(n):
        arr.append(int(input()))
    target=int(input("enter no which is to be search:"))   
    linear_search(n,arr,target)