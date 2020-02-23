i=0
sum=0
while i<100:
    i=i+1
    if i%3==0:
        sum=sum+i
print("1부터 100까지 3의 배수의 합은", sum, "입니다.")



i1=input("시작 값을 입력하시오: ")  
i2=input("종료 값을 입력하시오: ")
i1=int(i1)
i2=int(i2)
n=input("몇의 배수의 합계를 구할겁니까?: ")
n=int(n)
sum=0
i=i1
while i<=i2:
    if i%n==0:
        sum=sum+i
    i=i+1
print("%s부터 %s까지 %s의 배수의 합은 %s입니다." %(i1, i2, n, sum))
    