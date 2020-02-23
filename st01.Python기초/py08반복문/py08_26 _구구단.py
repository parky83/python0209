i1=input("시작 단수를 입력하세요: ")
i2=input("종료 단수를 입력하세요: ")
i1=int(i1)
i2=int(i2)
if i1<=i2:
    pass
else:
    temp=i1
    i1=i2
    i2=temp
for i in range(i1,i2+1,1):
    for ii in range(1,10,1):
        str= "%2s*%s=%3s" %(i, ii, i*ii)
        if ii==9:
            print(str, end=".")
        else :
            print(str, end=",")
    print()
    