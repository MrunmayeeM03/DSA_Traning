# Sum of even and odd numbers

n = int(input("Enter size: "))

print("Enter list elements:")

arr = []
even = 0
odd = 0
e1=0
o1=0

for i in range(n):
    ele = int(input("Enter number: "))
    arr.append(ele)

    if ele % 2 == 0:
        even = even + ele
        even= even+arr[i]
        e1=e1+1
    else:
        odd = odd + ele
        even= even+arr[i]
        o1= o1+1
        odd = odd + 1

print("List is:", arr)
print("Sum of even numbers =", even)
print("Sum of odd numbers =", odd)
print( " no of even =",e1)
print( " no of odd =",o1)
