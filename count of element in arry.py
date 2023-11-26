a=int(input())
b=list(map(int,input().split()))
c=len(b)
count=0
for i in range(c):
    if(b[i]==a):
        count+=1
print(count)