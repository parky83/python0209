import math

w=input("사각형의 밑변의 길이는 몇 m인가?")
h=input("사각형의 높이의 길이는 몇 m인가?")

#w=float(w)
#h=float(h)

try:
    w=float(w)
    h=float(h)
    area=w*h
    perimeter=2*(w+h)
    print("사각형의 면적은", area, "m이고\n둘레는", perimeter, "m입니다.")


except ValueError :
    print("길이가 실수가 아닙니다.")

