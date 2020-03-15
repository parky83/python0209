def parse_file(path):
    infile = open(path)
    spaces = 0
    tabs = 0
    lines = 0
    for line in infile:
        spaces += line.count(" ")
        tabs += line.count("\t")
        lines += 1

    infile.close()
    return spaces, tabs, lines


filename = input("파일 이름을 입력하시오: ")
sIn = "./st01.Python기초/py31파일처리/file/%s" % (filename)
spaces, tabs, lines = parse_file(sIn)
print("스페이스 수= %d, 탭의 수= %d, 라인의 수= %d" % (spaces, tabs, lines))
