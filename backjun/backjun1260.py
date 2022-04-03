import sys
from collections import deque

N, M, V = map(int,sys.stdin.readline().split())

nList = [sys.stdin.readline().strip().split() for _ in range(M)]



def dfs(dlist):
    global V
    global M

    # 작은 곳을 먼저 가기 위해 정렬
    dlist.sort()

    # 방문한 곳 체크
    visit.append(V)

    for i in range(M):
        


# def bfs(blist):




    






print(visit)