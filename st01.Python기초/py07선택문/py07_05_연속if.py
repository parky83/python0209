# py04_02_ifelse

# 하나의 점수를 입력 받고, 입력 받은 점수에 해당하는 학점을 출력하는 프로그램을 작성하시오.
# 입력 받는 정수는 0~100까지이고    
# 90점 이상이면 A,     90 이상이고 100 이하이면
# 80점 이상이면 B,     80 이상이고 90 미만이면
# 70점 이상이면 C,     70 이상이고 80 미만이면
# 60점 이상이면 D,     60 이상이고 70 미만이면
# 나머지는 F              60 미만이면

grade=input("점수를 입력하시오: ")
grade=float(grade)
if 90<=grade and grade<=100:
    print("A")
elif 80<=grade and grade<90:
    print("B")
elif 70<=grade and grade<80:
    print("C")
elif 60<=grade and grade<70:
    print("D")
else :
    print("F")