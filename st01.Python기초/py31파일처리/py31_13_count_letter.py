# ./file/proverbs.txt 파일 열기 
filename = input("파일 이름을 입력하시오: ").strip()
sIn = "./st01.Python기초/py31파일처리/file/%s" % (filename)
infile=open(sIn, "r")
freqs={}

# 파일의 각 줄에 대하여 문자를 추출한다. 각 문자를 사전에 추가한다.
for line in infile:
    for char in line.strip():
        if char in freqs:
            freqs[char]+=1
        else:
            freqs[char]=1

print(freqs)
infile.close()
