a=int(input())
b=list(map(int,input().split()))
c=set(b)
e=[]
if len(b)==len(c):
    print(*b)
else:
    for i in b:
        if i not in e:
            e.append(i)
    print(*e)
