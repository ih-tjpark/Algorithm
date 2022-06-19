#import heapq
from collections import defaultdict

def solution(tickets):
    '''
    heapq로는 문자열 reverse가 힘들어 포기

    tickets_dic = {}
    for t1,t2 in tickets:
        if t1 in tickets_dic:
            heapq.heappush(tickets_dic[t1],t2)
        else:
            tickets_dic[t1] = [t2]

    depart ='ICN'
    answer = [depart]
    while(depart in tickets_dic and tickets_dic[depart]):

        in_check = depart
        depart = heapq.heappop(tickets_dic[depart])
        # 알파벳 빠른 순서로 갔으나 경로가 존재하지 않을 시 다른 경로 탐색
        if (depart in tickets_dic) and not tickets_dic[depart] and tickets_dic[in_check]:
            temp = depart
            depart = heapq.heappop(tickets_dic[in_check])
            heapq.heappush(tickets_dic[in_check],temp) 
        answer.append(depart)
        #print(tickets_dic)
    '''
    answer = []
    tickets_dic = defaultdict(list)
    for depart, arrive in tickets:
        tickets_dic[depart].append(arrive)

    for key in tickets_dic:
        tickets_dic[key].sort(reverse=True)

    qlist = ['ICN']
    while qlist:
        depart = qlist[-1]

        # 순방향 경로 저장
        if tickets_dic[depart]:
            qlist.append(tickets_dic[depart].pop())
        else:
            # 순방향 길이 끊겼을 때 역방향 경로 저장
            answer.append(qlist.pop())
    answer.reverse()
    #print(answer)

    return answer