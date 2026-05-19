#remove duplicate charecter
s= "ABCDABBCCEEEFFADF"
print(s)
result=""
for i in range(len(s)):
    print(s[i])
    if s[i] :
        result= result + s[i]
        print(result)
