
# 2단의 구구단을 가로 출력하는 프로그램을 만드시오. 끝날 때는 마침표를 붙인다.
# 힌트. 출력할 문자열을 변수에 저장하고 마지막 한번만 변수값을 print()를 사용하야 출력해야 한다.

a=input("몇 단을 출력하시겠습니까? :")
a=int(a)
for x in range(1,10,1):
    b=a*x
    # x가 9이면 마침표를 찍고
    # x가 9가 아니면 콤마ㅏ를 찍어라
    if x==9 :
        print("%s *%2s =%3s" % (a, x, b), end=".")
    else :
        print("%s *%2s =%3s" % (a, x, b), end=", ")
