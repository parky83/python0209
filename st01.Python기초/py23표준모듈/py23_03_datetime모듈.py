#################################
# datetime 모듈의 사용법을 익힌다.
#
# datetime.now()	현재 년월일시분초 가져오기
# datetime.timedelta()	시간 가감로세스를 주어진 초만큼 정지
# datetime.replace()	시간 교체
#################################

# 모듈을 읽어 들입니다.
import datetime
#import time

########################
# 현재 년,월,일,시,분,초 출력하기
# 예시)  년 2020
#        월 3
#        일 2
#        시 15
#        분 15
#        초 58
# print(time.time())
nowTime = datetime.datetime.now()
print(nowTime)
print(nowTime.year)
print(nowTime.month)
print(nowTime.day)
print(nowTime.hour)
print(nowTime.minute)
print(nowTime.second)
print(nowTime.microsecond)

########################
# 시간 출력 방법
# 예시) 2020.03.02 15:15:58
str = "%2d:%2d:%2d" % (nowTime.hour, nowTime.minute, nowTime.second)
print(str)
########################
# 시간 출력 방법
# 예시) 2020년 03월 02일 15시 15분 58초
str = "%2d시 %2d분 %2d초" % (nowTime.hour, nowTime.minute, nowTime.second)
print(str)
########################
# 현재 시간이 오전/오후 인지를 출력하시오.
# 파이썬에서 오전/오후 구별할 방법 없음 시간으로 오전/ 오후 판별해야함.==>if 문 사용
# 예시) 현재 시간은 15시로 오후입니다!
# 오전 구분
hour = nowTime.hour  # 현재 시간
# 오후 구분


########################
# 계절을 확인합니다.
# 현재 날짜/시간을 구하고 월을 변수에 저장합니다.
# 조건문으로 계절을 확인합니다.
# 예시) 현재는 봄입니다.

def dateFormat(tm):
    str = "%04d-%02d-%02d %02d:%02d:%02d" % (tm.year,
                                             tm.month, tm.day, tm.hour, tm.minute, tm.second)
    return str


print(dateFormat(datetime.datetime.now()))

########################
# 특정 시간 이후의 시간 구하기 : datetime.timedelta() 메서드
# datetime.timedelta()로 시간 더하기 >> 현재에 1주 1일 1시간 1분 1초를 더해서 출력하시오.
# 예시) 현재 2020-03-02 16:42:06
#       수정 2020-03-10 17:43:07

now = datetime.datetime.now()
print("현재: ", dateFormat(now))
after = datetime.timedelta(
    weeks=1,
    days=1,
    hours=1,
    minutes=1,
    seconds=1
)
# print(after)
print("after: ", dateFormat(after+now))


before = datetime.timedelta(
    days=-100,
)
# print(before)
print("before: ", dateFormat(before+now))


########################
# 특정 시간 요소 교체하기 : replace() 메서드
# 예시) 현재 2020-03-02 16:44:19
#       수정 2021-03-09 16:44:19
print("수정: ", dateFormat(now.replace(year=2021, day=9)))
