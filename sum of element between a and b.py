a=int(input())
b=list(map(int,input().split()))
c,d=map(int,input().split())
p=[]
for i in range(len(b)):
    if c <= b[i] <= d and b[i] in b:
        p.append(b[i])
if len(p)==0:
    print("-1")
else:
    print(sum(p))
