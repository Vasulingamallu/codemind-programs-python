a=int(input())
b=list(map(int,input().split()))
c=[]
first=0
last=len(b)-1
while first<=last:
    c.append(b[first])
    if first!=last:
        c.append(b[last])
    first+=1
    last-=1
if len(c)%2!=0:
    c.append(0)
    print(*c)
else:
    print(*c)
