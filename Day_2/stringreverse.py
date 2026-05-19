s="learning python is very difficult from ashish sir"
ls= s.split()
print(ls)
ans=""

for x in range(len(ls)):
    ans=ans+ls[x][::-1]+" "
    print(ans)




