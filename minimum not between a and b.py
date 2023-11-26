a=int(input())
b=list(map(int,input().split()))
c,d=map(int,input().split())
p=[]
for i in range(len(b)):
    if c <= b[i] <= d and b[i] in b:
        p.append(b[i])
for j in p:
    if j==min(b):
        b.remove(j)
if len(b)==0:
    print("-1")
else:
    print(min(b))
