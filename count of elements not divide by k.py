a,b=map(int,input().split())
c=list(map(int,input().split()))
d=0
e=[]
for i in c:
    if i%b!=0:
        e.append(i)
print(len(e))
