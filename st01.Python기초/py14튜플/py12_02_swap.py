x=2
y=3
tmp=x
x=y
y=tmp
print("x=", x, "y=", y)

# 튜플을 사용하는 방법

x=2
y=3

print("x=", x, "y=", y)
(x,y)=(y,x) #튜플을 이용하여 swap하는 방법
print("x=", x, "y=", y)
