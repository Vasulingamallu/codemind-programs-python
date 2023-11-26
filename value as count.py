a=int(input())
b=list(map(int,input().split()))
c=0
d=set(b)
e=list(d)
for i in e:
    if i==b.count(i):
        c+=1
print(c)
