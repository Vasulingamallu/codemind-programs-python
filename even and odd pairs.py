a=int(input())
b=list(map(int,input().split()))
c=[]
d=[]
e=[]
for i in b:
    if i%2==0:
        c.append(i)
    else:
        d.append(i)
minlen=min(len(c),len(d))
for i in range(minlen):
    e.append(c[i])
    e.append(d[i])
if minlen<len(c):
    for i in range(minlen,len(c)):
        e.append(c[i])
elif minlen<len(d):
     for i in range(minlen,len(d)):
        e.append(d[i])
if len(e)%2!=0:
    e.append(0)
    print(*e)
else:
    print(*e)
