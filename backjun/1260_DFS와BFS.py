#1:30

import sys
from collections import defaultdict, deque


sys_input = sys.stdin.readline

N, M, V = map(int,sys_input().split())

dic = defaultdict(list)

for _ in range(M):
    N1, N2 = map(int,sys_input().split())
    dic[N1].append(N2)
    dic[N2].append(N1)

def bfs():
    que = deque([V])

    visited = [0] * M
    visited[V-1] = 1 
    result = []
    while(que):
        key = que.popleft()
        result.append(str(key))
        li = dic[key]
        li.sort()
        for i in li:
            if visited[i-1] == 0:
                visited[i-1] = 1 
                que.append(i)
    print(' '.join(result))

def dfs():
    visited = [0] * M
    visited[V-1] = 1
    stack = [V]
    result = []
    while(stack):
        key = stack.pop()
        result.append(str(key))
        li = dic[key]
        li.sort(reverse=True)
        for i in li:
            if visited[i-1] == 0:
                visited[i-1] = 1
                stack.append(i)
    print(' '.join(result))

dfs()
bfs()