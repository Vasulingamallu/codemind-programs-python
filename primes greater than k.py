a=int(input())
b=list(map(int,input().split()))
d=int(input())
c=[]
def prime(x):
    if x==1:
        return False
    for i in range(2,x):
        if x%i==0:
            return False
            break
    else:
        return True
for i in b:
    if prime(i):
        c.append(i)
e=0
for i in c:
    if d<=i:
        e+=1
print(e)
