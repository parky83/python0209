
# os 모듈을 읽어 들입니다.
import os

# 기본 정보를 몇 개 출력해봅시다.

# 폴더를 만들고 제거합니다[폴더가 비어있을 때만 제거 가능].

# 파일을 생성하고 + 파일 이름을 변경합니다.

# 파일을 제거합니다.


# 파일 존재 유무 체크
# os.path.isfile()을 사용하여 파일의 존재 여부를 확인할 수 있다.
# os.path.isfile() 메서드는 있으면 true, 없으면 false를 반환한다.
# 1. 상대 경로를 사용하는 경우
#      ../ 부모 폴더
#      ./ 현재 폴더
# 2. 절대 경로를 사용하는 경우
#      C:\Users\Public\kbpark\st01.Python기초\py22패키지\a.txt
#  현태 폴더에 phones.txt 파일이 존재하는지 확인한다.

print(os.getcwd())
# print(os.path.isfile("./st01.Python기초/py23표준모듈/phones.txt"))
if os.path.isfile("./st01.Python기초/py23표준모듈/phones.txt"):
    print("파일존재")
else:
    print("파일없음")


# 현재 폴더의 파일/폴더를 출력합니다.

# 현재 폴더의 파일/폴더를 구분합니다.

# 폴더를 읽어 들이는 함수
