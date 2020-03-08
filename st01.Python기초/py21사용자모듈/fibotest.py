# import 방식
# 모듈 import : import 모듈이름
#                   사용방법 : 모듈명.함수명
# 함수 import : from 모듈이름 import 모듈함수
# as import

import fibo


def main():
    # fibo.fib(500)
    # print()
    val = fibo.fib2(500)
    print(val)

# 이 모듈이 단독으로 사용되면 main()를 호출하라.


if __name__ == "__main__":
    main()
