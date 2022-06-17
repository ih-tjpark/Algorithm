def solution(N, number):
    m = [set() for _ in range(9)] # index = N의 갯수, 요소 = N개의 갯수만큼 계산된 값

    if N == number: return 1

    for i in range(1,8):
        m[i].add(int(str(N)*i)) # 반복되는 N 추가 N,NN,NNN...
        for j in range(i): 
            for x in m[j]:  
                for y in m[i-j-1]: 
                    # j갯수로 계산된 값들과의 사칙연산을 모두 저장 
                    m[i].add(x+y)
                    m[i].add(x-y)
                    m[i].add(x*y)
                    if y != 0: # 0으로 나눌 시 error 
                        m[i].add(x//y)

                if number in m[i]:
                    return i+1
    return -1