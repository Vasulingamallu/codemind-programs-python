a=int(input())
def prime(a):
    for i in range(2,(a//2)+1):
        if a%i==0:
            return False
            break
    else:
        return True
if a==2:
    print("0")
else:
    b=a
    c=a
    while prime(b)!=True and b!=1:
            b+=1
    while prime(c)!=True and c!=1:
            c-=1
    if b-a > a-c:
        print(a-c)
    else:
        print(b-a)
