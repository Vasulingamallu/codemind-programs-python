a=int(input())
b=list(map(int,input().split()))
t=[]
for i in b:
    if i==b.count(i):
        if i not in t:
            t.append(i)
if len(t)==0:
    print("-1")
else:
    h=(sum(t))/(len(t))
    v=format(h,".2f")
    print(v)
    
