a=int(input())
b=list(map(int,input().split()))
count=0
for i in range(len(b)-1):
    if((b[i-1]%2==0 and b[i] and b[i+1]%2==1) or (b[i+1]%2==0 and b[i] and b[i-1]%2==1)):
        count+=1
print(count)
        