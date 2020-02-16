
# 숫자가 아닌 것을 정수로 변환하려고 할 때
# a=int("안녕하세요")
# b=float("안녕하세요")

try:
    a=int("안녕하세요")
    print(a)
except ValueError :
    pass

# 숫자가 아닌 것을 실수로 변환 할 때
#a=int("52.273")
try: 
    a=int("52.273")
except ValueError:
    pass

# 소수점이 있는 숫자 형식의 문자열을 int() 함수로 변환 할 때