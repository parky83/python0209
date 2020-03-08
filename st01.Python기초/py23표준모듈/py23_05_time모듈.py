#################################
# time 모듈의 사용법을 익힌다.
#
# time.sleep(초)	동작 중인프로세스를 주어진 초만큼 정지
#################################
# time.time() # UNIX 타임
# 모듈을 읽어 들입니다.


import time
import datetime

def dateFormat(tm):
    str = "%04d-%02d-%02d %02d:%02d:%02d" % (tm.year,
                                             tm.month, tm.day, tm.hour, tm.minute, tm.second)
    return str


print(time.time())

print(dateFormat(datetime.datetime.now()), "지금부터 5초 동안 정지")
time.sleep(5)
print(dateFormat(datetime.datetime.now()), "프로그램을 종료합니다.")