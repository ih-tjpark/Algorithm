def solution(n,lost, reserve):
    # 체육복을 빌려야 되는 사람
    # set을 사용하는 이유 : 집합끼리 연산할 수 있음
    los = set(lost) - set(reserve)
    res = set(reserve) - set(lost)
    
    for x in res:
        if x-1 in los:
            los.remove(x-1)
        elif x+1 in los:
            los.remove(x+1)
    
    return n-len(los)