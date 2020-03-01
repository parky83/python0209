# 사용자 함수 만들기
# 두 개의 정수가 주어지면 두수 중에서 더 큰 수를 찾아서 이것을 반환하는 함수를 만들어보자. 

def getmax(x, y):
    result = None
    if x > y:
        reaut = x
    else:
        result = y
    return result


def myinput():
    try:
        n1 = input(mesg)
        n1 = int(n1)
        return n1
    except ValueError:
        pass


# 왜 main() 함수를 만들어 사용하는가?
# 최대한 전역변수를 사용하지 않는다
n1 = myinput("첫번째 정수 입력:")
n2 = myinput("두번째 정수 입력:")