import sys
#from queue import PriorityQueue
import heapq
import math

N = int(sys.stdin.readline())

numList = [sys.stdin.readline().strip() for _ in range(N)]
#print(numList)

# 중앙값 기준 작은값(max)과 큰값(min) 관리하는 heap
minheap=[]
maxheap=[]

# maxheap에 push
# maxheap이 minheap보다 크기가 2이상 커지면 max앞 을 minheap에 push


for i,n in enumerate(numList):
    
    heapq.heappush(maxheap, -int(n))
    
    if minheap:
        # maxheap에 minheap에서 제일 작은 값보다 큰 값이 들어오면 swap
        if -maxheap[0]>minheap[0]:
            temp = -heapq.heappop(maxheap)
            heapq.heappush(maxheap,-heapq.heappop(minheap))
            heapq.heappush(minheap, temp)
    
    if len(maxheap)>=len(minheap)+2:
        heapq.heappush(minheap, -heapq.heappop(maxheap))
    

    print(-maxheap[0])
