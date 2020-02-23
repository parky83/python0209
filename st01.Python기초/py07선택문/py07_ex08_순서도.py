a=1
b=2
a=int(a)
b=int(b)

c=0
while c<=30:
    c=a+b
    a=b
    b=c
print(c)
