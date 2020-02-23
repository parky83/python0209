def Add(var1, var2):
    result=var1+var2
    return result

def Minus(var1, var2):
    result=var1-var2
    return result

def Mul(var1, var2):
    result=var1*var2
    return result

def Div(var1, var2):
    try:
        result=var1/var2
    
    except ZeroDivisionError:
        result="0으로 나눌 수 없습니다."
    return result

a=2
b=4
r1=Add(a, b)
r2=Minus(a, b)
r3=Mul(a, b)
r4=Div(a, b)

print("Add: ", r1, "\nMinus: ", r2, "\nMul: ", r3, "\nDiv: ", r4)
