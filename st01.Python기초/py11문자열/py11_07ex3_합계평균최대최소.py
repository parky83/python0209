
def main():
    array1 = " 74 874 9883 73 9 73646 774 "
    print(array1)

    # 문자열 자르기-->리스트를 얻게 됨.
    array2 = array1.strip().split(" ")
    print(array2)

    # 문자열을 정수 리스트로 만든다.
    array3 = []
    for n in array2:
        n = int(n)
        array3.append(n)

    print(array3)

    # 정수 리스트를 오름차순으로 정렬하시오.
    array4 = sorted(array3)
    print(array4)

    # 정수 리스트에서 최대값을 찾는다.
    maximum = max(array4)
    #maximum = array4[-1]
    print("최대값은 %s" % (maximum))

    # 정수 리스트의 합계, 평균, 최대값 그리고 최소값을 구하시오.
    a = sum(array4)
    print("합계 %s" % (a))
    b = a/len(array4)
    print("평균 %s" % (b))
    c = max(array4)
    print("최대값 %s" % (c))
    d = min(array4)
    print("최소값 %s" % (d))

if __name__=="__main__":
    main()


