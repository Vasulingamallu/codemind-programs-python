a=int(input())
b=list(map(int,input().split()))
b.reverse()
for i in range(a):
    if b[i]%2!=0:
        print(len(b)-1-i)
        break
