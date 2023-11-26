a=int(input())
b=[]
c=str()
for i in str(a):
    if int(i)==6:
        b.append(9)
        pass
    else:
        b.append(int(i))
for j in b:
    c+=str(j)
print(int(c))