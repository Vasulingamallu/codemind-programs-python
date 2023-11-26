a=int(input())
b=list(map(int,input().split()))
c=[]
d=[]
for i in b:
    if i not in d:
        d.append(i)
for i in d:
    c.append(i)
    c.append(b.count(i))
print(*c)
