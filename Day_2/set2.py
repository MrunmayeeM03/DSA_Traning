n=int(input("Enter size: "))
print("Enter list of element:")
arr=[]
for i in range(n):
    ele=int(input("enter element:"))
    arr.append(ele)
for i in range (len(arr)):
    print(arr[i])

#----------------------------
#input types
# 1. a=int(input())   o/p 12
#     a=int(input())      22
#-----------------------------
#2. a,b =map(int,input().split())
#-----------------------------