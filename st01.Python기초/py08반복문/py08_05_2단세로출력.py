
#a=2
a=input("몇 단을 출력하시겠습니까? :")
a=int(a)
for x in range(1,10,1):
    b=a*x
    print("%s *%2s =%3s" % (a, x, b))
