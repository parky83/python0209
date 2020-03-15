
# 작업 순서
# 1. 모듈 또는 클래스 import
# 2. main() 메서드 만들기
#     인스턴스 생성
# 3. 이 모듈이 단독으로 사용되면 main()를 호출하라.
#    if __name__ == "__main__":
#    main()

# 코딩 하기
import FourCal

a = input("First num : ")
b = input("Second num : ")

a = int(a)
b = int(b)
c1 = FourCal.FourCal(a, b)  # 인스턴스 생성할 때 변수 지정
# c1=FourCal.FourCal(a,b)

print("a", c1.getVar()[0], "b", c1.getVar()[1])
print("두 수의 합은: ", c1.add())
print("두 수의 차는: ", c1.sub())
print("두 수의 곱은: ", c1.mul())
print("두 수의 나눗셈은: ", c1.div())

a = 5
b = 10
c1.setVar(a, b)  # 생성된 인스턴스의 변수를 바꿀 때

print("a", c1.getVar()[0], "b", c1.getVar()[1])
print("두 수의 합은: ", c1.add())
print("두 수의 차는: ", c1.sub())
print("두 수의 곱은: ", c1.mul())
print("두 수의 나눗셈은: ", c1.div())
