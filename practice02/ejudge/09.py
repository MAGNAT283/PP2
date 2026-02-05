n =int(input())
n2=list(map(int,(input().split())))
mx=max(n2)
mn=min(n2)
for i in range(n):
    if n2[i]==mx:
        n2[i]=mn
print(*n2)