
# 1부터 10까지의 합계를 구하고
# 그 합계를 sum에 저장하고 sum 값을 한번만 출력한다.

iStart=1
iEnd=10
sum1=0
for i in range(iStart, iEnd+1, 1):
    sum1=sum1+(i)
print(sum1)

# 1부터 100까지의 합계를 구하고
# 그 합계를 sum2 에 저장하고 sum2 값을 한번만 출력한다.
iStart=1
iEnd=100
sum2=0
for i in range(iStart, iEnd+1, 1):
    sum2=sum2+(i)
print(sum2)

# 100부터 sum2까지의 합계를 구하고
# 그 합계를 sum3 에 저장하고 sum3 값을 한번만 출력한다.
iStart=100
iEnd=sum2
sum3=0
for i in range(iStart, iEnd+1, 1):
    sum3=sum3+(i)
print(sum3)

# 반복되는 코드는 함수를 만들어서 사용
def get_sum(iStart, iEnd):
    sum = 0
    for i in range(iStart, iEnd+1,1):
        sum+=i
    str="%s부터 %s까지 합계는 %s입니다." %(iStart, iEnd, sum)
    print("함수", str)
    return sum


sum4=get_sum(1,10)
sum5=get_sum(1,100)
sum6=get_sum(100, sum5)
