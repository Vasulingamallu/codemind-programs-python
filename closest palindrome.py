a=int(input())
def ispalin(num):
   if str(num)==str(num)[::-1]:
       return True
def closest_palin(num):
    b=[]
    num1=num-1
    num2=num+1
    while True:
        if ispalin(num1):
            b.append(num1)
            break
        num1-=1
    while True:
        if ispalin(num2):
            b.append(num2)
            break
        num2+=1
    return b
b=closest_palin(a)
c=b[0]
d=b[1]
if a-c>d-a:
    print(d)
elif a-c==d-a:
    print(*b)
else:
    print(c)
