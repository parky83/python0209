
#  proverbs.txt 파일에서 줄 단위로 읽어서 output.txt 에 쓰시오 

import os.path
infile = open("./st01.Python기초/py31파일처리/file/proverbs.txt",
              "r", encoding="UTF-8")
s=infile.readline()
outfile = open("./st01.Python기초/py31파일처리/file/output.txt",
              "w", encoding="UTF-8")
outfile.write(s)
infile.close()
outfile.close()