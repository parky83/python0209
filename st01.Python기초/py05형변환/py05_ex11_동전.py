# 자동 판매기를 시뮬레이션하는 프로그램을 작성하여 보자. 
# 사용자는 1000원짜리 지폐와 500원짜리 동전, 100원짜리 동전을 사용할 수 있다. 
# 물건값을 입력하고 1000원권, 500원짜리 동전, 100원짜리 동전의 개수를 입력하면 
# 거스름돈을 계산하여서 동전으로 반환한다. 

price=input("물건갑을 입력하시오")
num_1000=input("\n받은 돈 중 1000원 지폐 개수는?")
num_500=input("\n받은 돈 중 500원 동전 개수는?")
num_100=input("\n받은 돈 중 100원 동전 개수는?")

num_1000=int(num_1000)
num_500=int(num_500)
num_100=int(num_100)

a=num_1000*1000+num_500*500+num_100*100
price=int(price)

b=a-price
# 거스름돈(500원 동전 개수)을 계산한다. 
num_500=b//500
m_500=b%500
c=b-num_500*500
    
# 거스름돈(100원 동전 개수)을 계산한다. 
num_100=c//100
m_100=c%100
d=c-num_100*100

# 거스름돈(10원 동전 개수)을 계산한다. 
num_10=d//10
m_10=d%10
e=d-num_10*10

# 거스름돈(1원 동전 개수)을 계산한다. 
num_1=e//1
m_1=e%1
f=e-num_1*1
    
# 출력
print("\n물건 금액은", price, "원이며 총 받은 돈은", a,"원 이므로")   
print("\n거스름 돈은 500원:.", num_500, "100원:", num_100, "10원:", num_10, "1원", num_1)
print("\n총", b,"원 입니다")
