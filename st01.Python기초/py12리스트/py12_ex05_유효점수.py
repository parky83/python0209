
# step1. ArrayList 인스턴스, list  만들기.
# step2. 심사 위원수를 입력 받는다.   
# step3. 심사 위원의 점수 입력 받아서 list에 저장. 
#     몇 번 입력 받아야 하는가? 심사 위원수 만큼
# step4. 합계를 구하는 메서드 만들기
#     1번방부터 마지막방 -1 까지 
# step5. 평균을 구하는 메서드 만들기. 
#     평균값 = (double)sum / ( list.size() - 2 ) 
# step6. ArrayLis 정렬하기.
# step7. 합계를 구하고 출력한다.
# step8. 평균을 구하고 출력한다.


ArrayList=[]
n=input("심사위원 수를 입력하시오 :")
n=int(n)
for i in range(0,n,1):
    try:
        grade=input("심사위원 점수 입력 :")
        grade=int(grade)
        if grade>=0:
            ArrayList.append(grade)               
        else :
            break # 반복문 종료

    except ValueError:
        print("점수를 다시 입력하시오")
gradeSort=sorted(ArrayList)
gradeSort.pop(-1)
gradeSort.pop(0)
gradeSum=sum(gradeSort)
gradeAvg=gradeSum/(n-2)
    
try:
    print("유효점수 %s\n합계 %s\n평균 %s" %(gradeSort, gradeSum, gradeAvg))    
    #gradeAvg=sum/i
    #print("성적의 평균은 %s 입니다." %(gradeAvg))
except NameError:
    pass    
