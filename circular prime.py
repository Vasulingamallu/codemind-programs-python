a=int(input())
b=str(a)[::-1]
def prime(a):
    for i in range(2,(a//2)+1):
        if a%i==0 or a==1:
            return False
    else:
        return True
if prime(a) and prime(int(b)):
    print("circular prime")
elif prime(a):
    print("prime but not a circular prime")
else:
    print("not prime")
