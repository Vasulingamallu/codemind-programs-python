def bin(num):
    d=0
    p=0
    while num>0:
        d+=(num%10)*(2**p)
        num//=10
        p+=1
    return d
a=int(input())
b=list(map(int,input().split()))
c=int("".join(map(str,b)))
print(bin(c))
