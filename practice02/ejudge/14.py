n=int(input())
n2=list(map(int, input().split()))
cnt=0
mx=0
for i in range(n):
    for j in range(i,n):
        if n2[i]==n2[j]:
            cnt+=1
            
    if cnt==mx:
        mx=min(n2[i],n2[j])
    elif cnt>mx:
        mx=cnt
        cnt=0
        
print(mx)
    