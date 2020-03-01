# 리스트의 CRUD3S
# C: create.
# R: read
# U: update
# D: delete
# S: search
# S: sort
# S: shuffle


############################
# 리스트 선언
array = []
arrat = list()
array = [273, 32, 103, "문자열", True, False, [0, 1], {"a": 1, "1": "ba"}, None]
print(type(array), array)
# 공백 리스트 생성
array = []
print(type(array), array)
# 문자 H, e, l, l, o를 요소로 가지는 리스트
array = ["H", "e", "l", "l", "o"]
print(type(array), array)
# 문자열 Hello를 요소로 가지는 리스트
array = ["Hello"]
print(type(array), array)

# 0, 1, 2, 3, 4를 요소가 가지는 리스트 생성
array = [0, 1, 2, 3, 4]
print(type(array), array)

# 공백 리스트 생성
# 문자열을 리스트로 변환. 문자 H, e, l, l, o를 요소로 가지는 리스트 생성
array = list("Hello")
print(type(array), array)
# 0, 1, 2, 3, 4를 요소가 가지는 리스트 생성
############################
array = [0, 1, 2, 3, 4]
print(type(array), array)
array = list(range(0, 5, 1))
print(type(array), array)

############################
# 리스트 요소 출력
# 리스트의 시작은 0번부터
# 리스트 Read : [] 선택 연산자 사용한다.
############################
array = [273, 32, 103, "문자열", True, False, [0, 1], {"a": 1, "1": "ba"}, None]
print(type(array[0]), array[0])
print(type(array[3]), array[3])
print(type(array[5]), array[5])
print(type(array[6]), array[6])
print(type(array[7]), array[7])
print(type(array[8]), array[8])
############################
# 리스트 출력
############################
print(type(array), array)

############################
# 리스트 슬라이싱
# 1. 선택 연산자 사용하는 방법.
############################
print("", array[0])
print("", array[1:3])
print("", array[-1])
print("", array[-3])

############################
# 리스트 요소 대입
# 리스트의 0번값을 문자열 "변경"으로 바꾸시오
############################
print("array[0]", array[0])
array[0] = "변경"
print("array[0]", array[0])

############################
# 리스트 요소 추가 : C. create
# 추가 : 리스트의 마지막에 넣는다. --> .append() 메서드
# 삽입 : 리스트의 중간에 넣는다. --> .insert() 메서드
############################
array.append("추가")
print("array", array)
array.insert(0, "삽입")
print("array", array)


############################
# 리스트 요소 삭제 : D. delete
# 메서드 방식 --> pop() 메서드 * 추천, 꺼낸걸 가지고 있을 수 있음
# 연산자 방식 --> del
############################
print("array", array)
array.pop(0)
print("array", array)
del array[0]
print("array", array)

############################
# 리스트 열거
############################
for i in array:
    print(i, end="\n")

############################
# 복잡한 리스트
# 1차원 리스트
# 2차원 리스트
# 3차원 리스트
############################


############################
# 리스트에 담을 수 있는 것은? 모든 유형
# 리스트 선언 ==> [], list()
# 리스트 대입 ==> =
# 리스트 추가(C) ==> append(), insert()
# 리스트 읽기(R) ==> [방번호]
# 리스트 수정(U) ==> [방번호] = 값
# 리스트 삭제(D) ==> pop()
# 리스트 정렬(S) ==> sorted()
# 리스트 찾기(S) ==> .find() + 반복문, .rfind() + 반복문
# 리스트 길이 ==> len()
# 리스트 출력
# 리스트 열거
# 리스트에 저장된 함수 실행하기
############################

############################
# 문자열 vs 리스트
############################
