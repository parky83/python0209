
import os
#########################
# readline() 파일에서 한 줄씩 읽기
print(os.getcwd())
print(os.path.isfile("./st01.Python기초/py31파일처리/file/phones.txt"))
infile = open("./st01.Python기초/py31파일처리/file/phones.txt",
              "r", encoding="UTF-8")
s = infile.readline()
print(s, end="")
s = infile.readline()
print(s, end="")
s = infile.readline()
print(s, end="")

infile.close()
#########################
# 반복문으로 파일에서 읽어서 모니터에 출력하기
infile = open("./st01.Python기초/py31파일처리/file/phones.txt",
              "r", encoding="UTF-8")

line = infile.readline()
while line != "":
    print(line, end="")
    line = infile.readline()

infile.close()

#########################
##
