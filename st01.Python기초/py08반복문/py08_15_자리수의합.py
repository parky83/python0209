x = input("정수를 입력하시오: ")
i1 = len(x)
i1 = int(i1)
y = x
x = int(x)
s = str(x)
i = i1
sum = 0
while i >= 0:
    a = 10**i
    p = x//a
    x = x-(p*a)
    sum = sum+p
    i = i-1
print(sum)


# 작업 순서
# 1. 문자열 정수의 길이를 구한다.
# 2. 0부터 길이 -1 까지 1씩 증가시키면서
#   2-1. 문자 한개를 꺼내 정수로 변환
#   2-2 sum+정수 를 한다.

# for문
sum = 0
for y1 in range(0, i1, 1):
    y2 = int(y[y1])
    sum = sum+y2
print(sum)


# 반복문
sum = 0
y1 = 0
while y1 < i1:
    y2 = int(y[y1])
    sum = sum+y2
    y1 = y1+1
print(sum)
