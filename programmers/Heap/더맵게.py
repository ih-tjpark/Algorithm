import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    for i in range(len(scoville)):     
        try:   
            # 가장 작은 수 POP
            scov1 = heapq.heappop(scoville)      
            if scov1 < K:
                # 두번째로 작은 수 pop
                scov2 = heapq.heappop(scoville)
                heapq.heappush(scoville , scov1 + scov2 * 2)
            else:
                answer = i
                break
        except:
            answer = -1
            break

    return answer