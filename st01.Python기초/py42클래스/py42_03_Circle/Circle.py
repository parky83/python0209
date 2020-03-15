
# 작업 순서 
# 1. 모듈 또는 클래스 import
# 2. 클래스명은 파스칼 표기법으로 정한다. 첫글자는 대문자로.
#     생성자 선언 : 인스턴스가 생성될 때 실행
#     소멸자 선언 : 소멸자는 인스턴스가 소멸할 때 실행
#     __str__() 메서드 오버라이딩
#     접근자( getter ) 메서드 선언. 비공개 인스턴스 변수 읽기
#     설정자( setter ) 메서드 선언. 비공개 인스턴스 변수 수정
#     사용자 메서스 선언
# 3. main() 메서드 만들기 
#     인스턴스 생성
# 4. 이 모듈이 단독으로 사용되면 main()를 호출하라.
#    if __name__ == "__main__":
#    main()


# 코딩 하기 
import math

class Circle(object):
    # 생성자
    def __init__(self, radius=0):
        self.radius=radius # 공개변수

    # 사용자 매서드
    def calcArea(self):
        result =math.pi*self.radius**2
        return result

    # 사용자 매서드
    def calcCircum(self):
        result = 2*math.pi*self.radius
        return result


        

def main():
    pass
# 단독 사용시 main()를 호출
if __name__=="__main__":
    main()
        
