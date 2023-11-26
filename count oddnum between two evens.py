n=int(input())
b=list(map(int,input().split()))
c=0
for i in range(len(b)-1):
    if((b[i-1]%2==0 and b[i]%2==1 and b[i+1]%2==0 )):
        c+=1
print(c)