a,b=map(int,input().split())
c=list(map(int,input().split()))
d=0
for i in range(len(c)):
    for j in range(i,len(c)):
        if sum(c[i:j+1])==b:
            d+=1
print(d)
