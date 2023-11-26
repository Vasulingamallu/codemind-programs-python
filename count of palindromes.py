a=int(input())
b=list(map(int,input().split()))
c=0
for i in b:
    if str(i)==str(i)[::-1]:
        c+=1
print(c)
