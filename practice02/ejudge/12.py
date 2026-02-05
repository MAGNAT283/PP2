n=int(input())
n2=list(map(int,input().split()))
for i in range(n):
    n2[i]=n2[i]*n2[i]
print(*n2)