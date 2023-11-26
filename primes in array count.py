a=int(input())
b=list(map(int,input().split()))
c=[]
def prime(n):
    if n==1:
        return False
    else:
        for i in range(2,(n//2)+1):
            if n%i==0:
                return False
                break
        else:
            return True
for i in b:
    if prime(i):
        c.append(i)
print(len(c))
