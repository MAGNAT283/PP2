n=int(input())
lst=input().split()
mx=int(lst[0])
for i in lst:
    i=int(i)
    if i>mx:
        mx=i
mx=str(mx)
ind = lst.index(mx)
print(ind+1)
