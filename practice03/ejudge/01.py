n = (input())
cnt=0
for i in range(len(n)):
    n2=int(n[i])
    if n2%2!=0:
        print("Not valid")
        break
    if n2%2==0:
        cnt+=1
if cnt==len(n):
    print("Valid")