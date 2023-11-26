a=int(input())
def sum1(x):
    b=x
    if b < 10 and b!=0:
         return b
    else:
        b=0
        while x>0:
            b+=x%10
            x//=10
        return sum1(b)
print(sum1(a))
