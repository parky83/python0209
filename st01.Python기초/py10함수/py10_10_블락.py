def get_sum(iStart, iEnd):
    sum = 0
    for i in range(iStart, iEnd+1,1):
        sum+=i
    str="%s부터 %s까지 합계는 %s입니다." %(iStart, iEnd, sum)
    print("함수", str)
    return sum


# 함수 호출
a=3
b=7
get_sum(a,b)

# 변수의 종류
# 전역변수 : a, b => 함수에서 접근이 가능
# 지역변수 : sum, i, iStart, iEnd
# 매개변수 : iStart, iEnd
