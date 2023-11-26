a=int(input())
b=list(map(int,input().split()))
c=[]
for i in b:
    if i%2!=0:
        c.append(i)
for i in b:
    if i%2==0:
        c.append(i)
print(*c)
