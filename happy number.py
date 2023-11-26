def hapnum(n):
    seen=set()
    while n!=1 and n not in seen:
        seen.add(n)
        n=sum(int(dig)**2for dig in str(n))
    return n==1
num=int(input())
if hapnum(num):
    print("True")
else:
    print("False")
