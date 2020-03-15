
# 작업 순서 
# 1. 모듈 또는 클래스 import
# 2. main() 메서드 만들기 
#     인스턴스 생성
# 3. 이 모듈이 단독으로 사용되면 main()를 호출하라.
#    if __name__ == "__main__":
#    main()

# 코딩 하기 

import FourCal
import MoreFourCal


def main():
    c1=FourCal.FourCal(2,4)
    c2=MoreFourCal.MoreFourCal(5,7)
    val=c2.pow()
    print(val)
    
    val=c2.add()
    print("add:", val)
    
if __name__=="__main__":
    main()