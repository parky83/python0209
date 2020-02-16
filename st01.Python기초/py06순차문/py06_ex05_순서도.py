# py06_ex05_순서도

s=input("s를 입력하시오")
s=float(s)
m=s//60
s=s%60
#s=(s-m*60)
print("60으로 나누었을 때 몫은", m)
print("나머지는", s, "입니다.")