# 정수를 입력을 받습니다.
# 입력 받은 문자열을 정수로 바꿉니다.
number = input("정수 입력> ")
number = int(number)

# 문자열로 변환
number = str(number)


#######################################
# 방법1. 문자열을 사용하는 방법
# 방법2. 나머지를 사용하는 방법
#######################################

#######################################
# 방법1. 문자열을 사용하는 방법
#######################################
# 마지막 자리 숫자를 추출
last_character = number[-1]

# 숫자로 변환하기
last_number = int(last_character)

if last_number == 0 \
    or last_number == 2 \
    or last_number == 4 \
    or last_number == 6 \
    or last_number == 8:
    # 짝수 확인
    print("짝수입니다")
else:
    # 홀수 확인
    print("홀수입니다")


#######################################
# 방법2. 나머지를 사용하는 방법
#######################################
if number % 2 == 0:
    # 짝수 조건
    print("짝수입니다")
else:
    # 홀수 조건
    print("홀수입니다")
