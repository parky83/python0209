a=input("a를 입력하시오 :")
b=input("b를 입력하시오 :")

# 문자열에는 *, + 연산자만 있고 / 연산자는 없다.
try:
    a=int(a)
    b=int(b)
    avg = (a+b) / 2
except ValueError:
    pass


if avg >=160 :
    print("합격")
else :
    print("불합격")