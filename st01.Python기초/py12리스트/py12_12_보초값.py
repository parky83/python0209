
# 무한 반복문

glist=[]
while True: # 무한루프
    try:
        grade=input("성적을 입력하시오 :")
        # grade=int(grade)
        grade=float(grade)
        if grade>=0:
            glist.append(grade)               
        else :
            break # 반복문 종료

    except ValueError:
        print("성적을 다시 입력하시오")
    
n=len(glist)
gradeSum=sum(glist)
gradeAvg=gradeSum/n
#print(glist, "평균", gradeAvg) 

try:
    print("학생 %s명의 성적 %s의\n총합은 %s이며 평균은 %s입니다." %(n, glist, gradeSum, gradeAvg))    
    #gradeAvg=sum/i
    #print("성적의 평균은 %s 입니다." %(gradeAvg))
except NameError:
    pass    


