a=int(input())
b=[]
def prime(a):
    for i in range(2,a):
        if a%i==0:
            return False
    else:
        return True
for i in range(2,a):
    if prime(i):
        b.append(i)
w=0
for i in b:
    for j in b:
        if i*j==a and i!=j:
            print(i,j)
            w+=1
            break
        if w==1:
            break
    if w==1:
        break
if w==0:
    print("-1")
