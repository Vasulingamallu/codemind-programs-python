a=int(input())
b=list(map(int,input().split()))
c,d=map(int,input().split())
f=max(b)
g=[]
for i in range(c,d+1):
    g.append(i)
if f in g:
    print("-1")
else:
    print(f)
