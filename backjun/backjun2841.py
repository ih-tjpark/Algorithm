import sys
from collections import deque

N, P = map(int,sys.stdin.readline().split())

data=[(sys.stdin.readline().strip().split()) for i in range(N)]

lines=[ []*n for n in range(N)]
count = 0
#print(lines)

for line,plat in data:

    line = int(line)-1
    plat = int(plat)

    #print(line,plat)
    #if line == '1':
    # 아무것도 없으면 넣기
    if not lines[line]:
        lines[line].append(plat)
        
        count+=1

    else:
        # 마지막 요소보다 크면 넣기
        if lines[line][-1] < plat:
            lines[line].append(plat)
            count+=1

        # 마지막 요소랑 같으면 통과
        elif lines[line][-1] == plat:
            continue

        # 마지막 요소보다 작으면 자기보다 같거나 작은 요소가 나올때까지 반복
        else:
            for i in range(len(lines[line])+1):
                if not lines[line] or plat > lines[line][-1]:
                    lines[line].append(plat)
                    count+=1
                    break
                elif plat == lines[line][-1]:
                    break
                else:
                    lines[line].pop()
                    count+=1
                #print(lines)

    #print(count)
    #print(lines)
    

#print(lines)
print(count)
        
        

        
