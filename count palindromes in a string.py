a=input()
b=list(a.split())
def ispal(x):
    x=x.lower()
    if x==x[::-1]:
        return True
    else:
        return False
c=0
for i in b:
    if ispal(i):
        c+=1
print(c)
