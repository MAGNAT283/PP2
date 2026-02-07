n=int(input())
cnt={}
for i in range(n):
    phone=input().strip()
    cnt[phone]=cnt.get(phone,0)+1
answer=0
for value in cnt.values():
    if value==3:
        answer+=1
print(answer)