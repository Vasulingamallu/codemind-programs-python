for _ in range(int(input())):
    n,a,b,k=map(int,input().split())
    a1=n//a
    b1=n//b
    c1=n//(a*b)
    if (a1+b1-2*c1)>=k:
        print("Win")
    else:
        print("Lose")
