a=int(input())
b=list(map(int,input().split()))
c,d=map(int,input().split())
for i in range(c,d+1):
    if i in b:
        b.remove(i)
if len(b)==0:
    print("-1")
else:
    print(*b)
