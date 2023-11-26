a=input()
b=list(a.split())
c=[]
for i in b:
    v=0
    g=0
    v=(ord(min(i)))
    g=(ord(max(i)))
    c.append(abs(v-g))
print(*c)
