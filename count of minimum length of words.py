a=input("enter the string:")
b=list(a.split(' '))
c=100
m=0
for i in b:
    m=len(i)
    if c>m:
        c=m
print(c)
