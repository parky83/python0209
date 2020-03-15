
#########################
## 키보드 입력을 파일에 쓰는 프로그램을 작성하여 본다.
#########################
import os.path
if os.path.isfile("keyboard.txt"):
    ex=input("동일한 이름의 파일이 이미 존재합니다. 삭제하겠습니까?(Y/N) :")
    if ex.upper()=="Y":
        os.remove("keyboard.txt") #지우는 방법??
        outfile = open("keyboard.txt", "w", encoding="UTF-8")
        while True:
            a=input("입력 :")
            if a!="exit":
                #string="%s\n" %(a)
                outfile.write("%s\n" %(a))
            else:
                outfile.close()
                break
    elif ex.upper()=="N":
        pass
    
else:    
    outfile = open("keyboard.txt", "w", encoding="UTF-8")
    while True:
        a=input("입력 :")
        if a!="exit":
            #string="%s\n" %(a)
            outfile.write("%s\n" %(a))
        else:
            outfile.close()
            break