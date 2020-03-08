# 1. 파일 읽고 문자열에 텍스트 저장
# 2. 딕셔너리 table을 만든다.
# 3. 문자열을 split() 해서 array 리스트로 만든다.
# 4. 반복문을 사용하여 array 리스트를 루프 돌면서
#   1. 리스트 요소에서 첫글자를 추출한다. 선택 연산자 [] 사용
#       val = array[i][0] 또는 val=i[0]
#   2. 대문자와 소문자를 구분하지 않도록 소문자로 치환한다.
#       val=val.lower()
#   3. 딕셔너리 table에서 키값 중에 val이 있는지 찾는다.
#       ==> table에서 찾을때는 get()메서드나 in 연산자 사용
#   4. 찾았다면 table[val]=table[val]+"-"
#       아니면 table[val]="-"
# 5. 찾기가 끝나면 table 출력한다.


string = """This was a great help. 
I applied this method to similiar problem 
and rather than concat a SELECT statement 
I created an event scheduled every couple 
hours to rebuild a view that pivots n amount 
of rows from one table into n columns on the other. 
It is a big help because before I was rebuilding 
the query using PHP on every execution of the SELECT. 
Even though views can not leverage Indexes, 
I am thinking filtering performance will not 
be an issue as the pivoted rows->columns 
represent types of training employees at a 
franchise have so the view will not ever break 
a few thousand rows."""
string = string.upper()
array1 = string.replace("\n", "")
print(array1)
array1 = array1.split(" ")

table = {}
for i in array1:
    if table.get(i[0]) == None:
        table[i[0]] = [1, "-"]
    else:
        table[i[0]][0] = table[i[0]][0]+1
        table[i[0]][1] = table[i[0]][1]+"-"

K = sorted(table)
result = {}
for i in K:
    result[i] = table.get(i)
    print(i, result[i])
    
#for item in result.items():
#    print(item)


#
ALP=input("어떤 문자의 갯수를 가져올까요?: ")
print(result[ALP][1].count("-"))