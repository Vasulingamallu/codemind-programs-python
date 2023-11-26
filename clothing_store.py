a=int(input())
b=list(map(int,input().split()))
c=0
d=0
for i in range(len(b)):
    c=0
    for j in range(i+1,len(b),+1):
        if b[i]==b[j]:
            c+=1
    d=d+c%2
print(d)    
