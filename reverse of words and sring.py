t=input()
b=t.split()
print(b)
for i in range(len(b)):
    b=b[i][::-1]
print("  ".join(b))
