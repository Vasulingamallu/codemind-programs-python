n=int(input())
a=list(map(int,input().split()))
c=len(a)-1
for i in range(c,1,-1):
       if a[i]%2==1:
           print(a[i])
           break
       
