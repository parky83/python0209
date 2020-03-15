filename = input("파일 이름을 입력하시오: ").strip()
sIn = "./st01.Python기초/py31파일처리/file/%s" % (filename)
# print(sIn)
infile = open(sIn, "r")
for line in infile:
    line = line.rstrip()
    word_list = line.split()
    for word in word_list:
        print(word)
infile.close()
