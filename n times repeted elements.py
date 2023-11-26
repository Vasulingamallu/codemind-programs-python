a=int(input())
b=list(map(int,input().split()))
c=int(input())
g=[]
for i in b:
    if b.count(i)==c:
        if i not in g:
            g.append(i)
if len(g)==0:
    print("-1")
else:
    print(*g)
