num1=input("숫자1 입력: ")
num2=input("숫자2 입력: ")

try:
    num1=int(num1)
    num2=int(num2)
    res=num1/num2
    print(res)
except ValueError as ex:
    print("ValueError", ex)
except ZeroDivisionError as ex:
    print("ZeroDivisionError", ex)