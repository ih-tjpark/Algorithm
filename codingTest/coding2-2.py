def solution(n, actions):

    # 0번째 요소 : 자기안에 들어가 있는 가방 번호
    # 1번째 요소 : 자기가 들어간 가방 번호
    link_list = [[[],0] for _ in range(n)]

    for act in actions:

        action = act.split(' ')
        #print(action)

        num = [int(a)-1 for a in action if a.isnumeric()]
        #print(num)
        
        
        if 'PUT' == action[0]:
            if link_list[num[0]][1] == 0 and link_list[num[1]][1]== 0:
                link_list[num[0]][1] = num[1]+1
                link_list[num[1]][0].append(num[0])
            else: return -1
        
        if 'SET' == action[0]:
            if link_list[num[0]][1] == 0:
                inner_bag = link_list[num[0]][0]
                for ib in inner_bag:
                    link_list[ib][1] = 0

                link_list[num[0]][0] = []
            else:
                return -1
        
        if 'SWAP' == action[0]:
            if link_list[num[0]][1] == 0 and link_list[num[1]][1]== 0:
                
                for li1 in link_list[num[0]][0]:
                    link_list[li1][1] = num[1]+1

                for li2 in link_list[num[1]][0]:
                    link_list[li2][1] = num[0]+1

                temp = link_list[num[0]][0]
                link_list[num[0]][0] = link_list[num[1]][0]
                link_list[num[1]][0] = temp

            else: return -1
        #print(link_list)
    floor=0
    for i, li in enumerate(link_list):
        # 바닥에 놓여진 갯 수 카운트
        if li[1] == 0:
            floor+=1
        # 자기보다 작은 번호의 가방안에 들어간 경우
        if i+1 > li[1] and li[1] !=0:
            return -1
    return floor

n = 3
actions = ["PUT 1 INSIDE 2","PUT 3 INSIDE 1"]
print(solution(n,actions))