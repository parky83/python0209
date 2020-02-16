a=input("첫번째 수를 입력하시오: ")
b=input("두번째 수를 입력하시오: ")
c=input("세번째 수를 입력하시오: ")

try:
    a=int(a)
    b=int(b)
    c=int(c)
    if a<b and a<c :
        print("가장 작은 수는 ", a)
    elif b<c :
        print("가장 작은 수는 ", b)
    else :
        print("가장 작은 수는 ", c)

except ValueError:
    print("입력값이 정수가 아닙니다.")
