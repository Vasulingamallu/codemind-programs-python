a,b=map(int,input().split())
if a==0 and b%2==0 and b!=0:
    print("YES")
elif b==0 and a%2==0 and a>0:
    print("YES")
elif a%2==0 and b%2!=0 and a>1:
    print("YES")
elif b%2==0 and a%2!=0 and b>1:
    print("YES")
elif a%2==0 and b%2==0 and a>1 and b>1:
    print("YES")
else:
    print("NO")
