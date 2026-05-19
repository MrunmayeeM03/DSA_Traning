no = int(input("Enter No: "))

n1 = no % 10      # last digit
n2 = int(str(no)[0])   # first digit

res = n1 + n2

print("Sum =", res)
