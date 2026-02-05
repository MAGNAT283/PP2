n=int(input())
n2=2
while n2<=n:
    if n2!=n:
        n2*=2
    else:
        print("YES")
        break
else:
    print("NO")