a=int(input())
b=list(map(int,input().split()))
c=set(b)
d=list(c)
v=[]
for i in d:
    if i%2!=0:
        v.append(i)
print(sum(v))
