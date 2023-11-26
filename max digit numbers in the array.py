a=int(input())
b=list(map(int,input().split()))
c=0
d=str(max(b))
for i in b:
    if len(d)==len(str(int(i))):
            c+=1
print(c)
