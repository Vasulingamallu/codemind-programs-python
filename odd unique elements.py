a=int(input())
b=list(map(int,input().split()))
c=set(b)
d=list(c)
e=0
for i in d:
    if i%2!=0:
        e+=1
print(e)
