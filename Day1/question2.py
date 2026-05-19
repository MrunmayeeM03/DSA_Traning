i = 1
j = 10

while i < j:
    print(i, "\t", j)
    i = i + 1
    j = j - 1

a = 1
b = 10

while a <= 5:
    if a == 3 and b == 8:
        a = a + 1
        b = b - 1
        continue

    print(a, b)

    a = a + 1
    b = b - 1
    