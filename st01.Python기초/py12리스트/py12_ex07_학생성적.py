# 1. List 만들기.
# 2. 학생수 입력 받기. 최소 4명이상
# 3. 학생 성적 입력 받기. 몇 번 입력 받아야 하는가?
# 4. 3번 학생의 성적을 100점으로 바꾸시오.
# 5. list에서 마지막 학생 삭제.
# 6. list에서 첫번째 값을 출력하시오.
# 7. 평균을 구하고 출력.

gradeSum=0
glist=[]
while True:
    n=input("학생수를 입력하시오 :")
    n=int(n)
    if n<4:
        print("학생수는 최소 4 이상이어야 합니다.")
    else:
        break       
# 여기까지.. 아래 하던 중임.
for i in range(0,n,1):
    try:
        grade=input("성적을 입력하시오 :")
        grade=int(grade)
        gradeSum=gradeSum+grade
        if grade>=0:
            glist.append(grade)               
        else :
            break # 반복문 종료  
    except ValueError:
        print("성적을 다시 입력하시오")
#gradeSum=sum(glist)
gradeAvg=gradeSum/n
#print(glist, "평균", gradeAvg)  
try:
    print("학생 %s명의 성적 %s의\n총합은 %s이며 평균은 %s입니다." %(n, glist, gradeSum, gradeAvg))    
    #gradeAvg=sum/i
    #print("성적의 평균은 %s 입니다." %(gradeAvg))
except NameError:
    pass    
