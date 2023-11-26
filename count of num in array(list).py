n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(len(a)):
    if n==a[i]:
        c+=1
print(c)