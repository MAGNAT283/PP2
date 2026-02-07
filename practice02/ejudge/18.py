n=int(input())
st={}
for i in range(1,n+1):
    s=input().strip()
    if s not in st:
        st[s]=i
for s in sorted(st):
    print(s,st[s])