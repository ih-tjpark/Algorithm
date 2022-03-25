import sys
K,L = map(int,(sys.stdin.readline().split()))

dict={}

for i in range(L): 

    sys_input = sys.stdin.readline().strip()
    
    
    dict[sys_input]=i

#item[1] = dict의 value
result = sorted(dict.items(),key = lambda item: item[1])
#print(result)

for i in range(K):
    # 수강인원 보다 적게 신청한경우 break
    if len(result)<=i:
        break
    print(result[i][0])