# 13:30
# 모든 트럭이 건널 때 최소 시간
# 다리는 weight이하 무게 견딜 수 있음
# 다리 길이, 무게, 트럭 무게

from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    que = deque()
    arrive = 0
    time= 0

    cur_weight = weight
    truck_idx = 0

    while arrive < len(truck_weights):
        time += 1
        if que:
            t_weight, start_time = que[0]
            
            # 제일 앞에 있는 트럭이 지나갈 경우
            if time - start_time >= bridge_length:
                que.popleft()
                cur_weight += t_weight
                arrive += 1
            
            # 트럭이 들어갈 수 있는 경우
            # 1.트럭 무게가 현재 다리가 수용할 수 있는 무게 이하인 경우
            # 2.다리 길이 만큼 트럭이 꽉 차지 않은 경우
            if len(truck_weights) > truck_idx and \
                cur_weight >= truck_weights[truck_idx] and \
                len(que) < bridge_length:
                
                cur_weight -= truck_weights[truck_idx]
                que.append([truck_weights[truck_idx], time])
                truck_idx += 1
                
            # 트럭이 들어갈 수 없는 경우
            else:
                pass
                
            
        else:
            que.append([truck_weights[truck_idx],time])
            cur_weight -= truck_weights[truck_idx]
            truck_idx += 1
            
    answer = time
    
    return answer