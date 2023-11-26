a=input()
b=list(a.split())
c=[]
d=[]
for i in b:
    c.append(ord(min(i)))
    d.append(ord(max(i)))
print(sum(d)-sum(c))
