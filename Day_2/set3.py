# accept values from user find sum of list

n = int(input("Enter number of elements: "))

lst = []

for i in range(n):
    value = int(input("Enter value: "))
    lst.append(value)

total = sum(lst)

print("List is:", lst)
print("Sum of list =", total)


