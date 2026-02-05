n=int(input())
if n>1:
    cnt=1
for i in range(1,n):
    if n%i==0:
        cnt+=1
if cnt==2:
    print("Yes")
else:
    print("No")