def binary_search(n,arr,target):
    flag=False
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if target==arr[mid]:
            flag=True
            low=mid
            break
        elif target<arr[mid]:
            high = mid-1
        elif target>arr[mid]:
             low=mid+1
             print("search is successfull")
             return
        print("search is unccessfull")
             
if __name__ == '__main__':
     n= int(input("enter size:"))
     arr=[]
     for i in range(n):
              arr.append(int(input()))
     target=int(input("enter no which is to be search:"))   
     binary_search(n,arr,target)
