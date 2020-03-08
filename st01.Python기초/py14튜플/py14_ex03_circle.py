import math # pi=3.14..를 사용하기 위해서 

def calCircle(r):
    circum=2*math.pi*r
    area= math.pi*r**2
    return(area, circum)

def main():
    radius=input("원의 반지름을 입력하시오: ")
    radius=float(radius)
    (a, c)=calCircle(radius) # 튜플로 반환 안됨
    T=calCircle(radius) # 튜플로 반환
    #print(type(T), T)
    print("원의 넓이는 %10.4f 이고 원의 둘레는 %10.4f 이다." %(T[0], T[1]))    
    #print("원의 넓이는 "+str(a)+" 이고 원의 둘레는 "+str(c)+" 이다.")    
    print(a, type(a))
    print(c, type(c))
    print(T, type(T))
    #T[0]=100
    #print(T)
    
if __name__=="__main__":
    main()