n =int(input())
n2=list(map(int,input().split()))
seen = set()
for i in range(n):
    if i not in seen:
        print("YES")
        seen.add(i)
    else :
        print("NO")