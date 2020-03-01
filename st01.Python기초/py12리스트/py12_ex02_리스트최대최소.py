
glist=[]
for i in range(0,10,1):
    try:
        grade=input("정수를 입력하시오 :")
        grade=int(grade)
        if grade>=0:
            glist.append(grade)               
        else :
            break # 반복문 종료

    except ValueError:
        print("정수를 다시 입력하시오")
        
gradeSort=sorted(glist)
gradeMax=gradeSort[-1]
gradeMin=gradeSort[0]
#print(glist, "평균", gradeAvg)    
    
try:
    print("최소값은 %s\n최대값은 %s입니다." %(gradeMin, gradeMax))    
    #gradeAvg=sum/i
    #print("성적의 평균은 %s 입니다." %(gradeAvg))
except NameError:
    pass    
