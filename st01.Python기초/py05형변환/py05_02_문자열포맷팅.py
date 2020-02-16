# %s 문자열 
# %d 10진 정수

# 문자열 포맷팅
print("I eat %d apples." % 3)

number =10
day= "three"
print("I ate %d apples. I was sick for %s days." % (number, day))

# 정렬과 공백
print("%10s" % "hi")  # 공백 채우기 유용함
print("%-10sjane." % "hi")

# 소수점 표현
"%0.4f" % 3.42134234
"%10.4f" % 3.42134234
