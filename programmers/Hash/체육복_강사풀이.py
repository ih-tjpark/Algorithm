def solution(n,lost, reserve):
    # ü������ ������ �Ǵ� ���
    # set�� ����ϴ� ���� : ���ճ��� ������ �� ����
    los = set(lost) - set(reserve)
    res = set(reserve) - set(lost)
    
    for x in res:
        if x-1 in los:
            los.remove(x-1)
        elif x+1 in los:
            los.remove(x+1)
    
    return n-len(los)