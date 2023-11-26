for i in range(int(input())):
    a=int(input())
    def prime(a):
        for i in range(2,(a//2)+1):
            if a%i==0:
                return False
        else:
            return True
    b=a
    c=a
    while prime(b)!=True and b!=1:
        b+=1
    while prime(c)!=True and c!=1:
        c-=1
    if b-a >= a-c:
        print(c)
    else:
        print(b)
