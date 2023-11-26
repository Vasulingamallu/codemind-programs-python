b=int(input())
a=list(map(int,input().split()))
c=0
d=0
for i in range(len(a)):
    if i%2==0:
        c+=a[i]
    else:
        d+=a[i]
print(c-d)
