a=int(input())
b=list(map(int,input().split()))
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
v=sum(c)/len(c)
print("{:.2f}".format(v))
