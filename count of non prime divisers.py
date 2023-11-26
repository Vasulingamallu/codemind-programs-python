a=int(input())
b=[a]
def prime(a):
    for i in range(2,(a//2)+1):
        if a%i==0 or a==1:
            return False
            break
    else:
        return True
for i in range(1,a+1):
    if a%i==0 and prime(i)!=True:
        b.append(i)
print(len(b))
