# ����� �Լ� �����
# �� ���� ������ �־����� �μ� �߿��� �� ū ���� ã�Ƽ� �̰��� ��ȯ�ϴ� �Լ��� ������. 

def getmax(x, y):
    result = None
    if x > y:
        reaut = x
    else:
        result = y
    return result


def myinput():
    try:
        n1 = input(mesg)
        n1 = int(n1)
        return n1
    except ValueError:
        pass


# �� main() �Լ��� ����� ����ϴ°�?
# �ִ��� ���������� ������� �ʴ´�
n1 = myinput("ù��° ���� �Է�:")
n2 = myinput("�ι�° ���� �Է�:")