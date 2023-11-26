s=input()
v=['a','e','i','o','u','A','E','I','O','U']
c=0
for i in s:
    for a in range(len(v)):
        if i==v[a]:
             c+=1
             break
if c>=5:
    print("true")
else:
    print("false")