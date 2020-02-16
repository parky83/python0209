# 문자열을 입력 받고 숫자인지 문자인지 판별하는 프로그램을 작성하시오.

ch=input("숫자나 문자를 입력하시오: ")

if "a"<=ch and ch<="z" or "A"<=ch and ch<="Z":
    print("영문자입니다.")