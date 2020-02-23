i=0
grade=0
sum=0
while grade>=0:
    grade=input("성적을 입력하시오 :")
    grade=int(grade)
    if grade>=0:
        sum=sum+grade
        i=i+1
 
gradeAvg=sum/i
print("성적의 평균은 %s 입니다." %(gradeAvg))


# 무한 반복문

i=0
grade=0
sum=0
while True: # 무한루프
    grade=input("성적을 입력하시오 :")
    grade=int(grade)
    if grade>=0:
        sum=sum+grade
        i=i+1
    else :
        break # 반복문 종료
    
 
gradeAvg=sum/i
print("성적의 평균은 %s 입니다." %(gradeAvg))