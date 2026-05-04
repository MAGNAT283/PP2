n=int(input())
n1=list(map(int,input().split()))
cnt=n1[0]
for i in range(n):
    if n1[i] < cnt and n1[i]>0:
        cnt=n1[i]

if cnt<0:
    print(-1)
else:
    print(cnt)
