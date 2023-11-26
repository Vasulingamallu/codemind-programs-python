a=int(input())
b=list(map(int,input().split()))
c=[]
for i in b:
    i=abs(i)
    c.append(len(str(int(i))))
print(*c)
