a,b=map(int,input().split())
c=list(map(int,input().split()))
d=list(map(int,input().split()))
e=[]
r=[]
for i in c:
    if i  not in d:
        e.append(i)
for j in d:
    if j not in c:
        e.append(j)
for i in e:
    if i not in r:
        r.append(i)
print(*r)
