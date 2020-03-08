# 1. 문자열을 split() 해서 array 리스트를 만든다.
# 2. 반복문을 사용하여 array 리스트를 루프를 돌면서 딕셔너리 table에서 찾는다.
# 3. 2.1 찾았다면 바꾼다. replace()
# 출력한다. 문자열 메서드 join() 을 사용하는 것으로 작성한다.

table={"B4": "Before",
    "TX": "Thanks",
    "BBL": "Be Back Later",
    "BNCU": "Be Seeing You",
    "HAND": "Have A Nice Day"}

print(table)

입력문장=input("번역할 문장을 입력하시오: ")
array=입력문장.split(" ")

#for i in range(0,len(array),1):
#    value = table.get(array[i])  #   
#    if value == None:
#        pass
#    else:
#        입력문장=입력문장.replace(array[i], value)
#print(입력문장)


#result=""
for i in array:
    value = table.get(i)  #   
    if value == None:
        pass
        #result=result + i + " "
    else:
        입력문장=입력문장.replace(i, value)
        #result=result + value + " "
#print(result)
print(입력문장)
