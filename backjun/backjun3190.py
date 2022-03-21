# import sys
# from collections import deque 

# N =int(sys.stdin.readline())
# K =int(sys.stdin.readline())

# apple = [(sys.stdin.readline().strip().split()) for i in range(K)]

# L = int(sys.stdin.readline())

# direct = [(sys.stdin.readline().strip().split())for i in range(L)]

# D = [(0,1),(1,0),(0,-1),(-1,0)]
# DN=0
# print(apple)
# print(direct)

# lines=[ [0]*N for n in range(N)]
# lines[0][0]=1

# head = [0,1]
# tail = [0,0]
# #deq = deque(lines)
# print(lines)

# print(apple


#while 1:
# for go, dir in direct:

    
#     for g in int(go):

        
#         head[0]=head[0]+dir[DN][0]
#         head[1]=head[0]+dir[DN][1]


#     #이동 시 벽에 부딪히거나 자기 몸에 부딪히면 끝
#     if head[0] >=N or head[1] >=N:
#         break

    #사과가 없으면 head로 이동 tail삭제
    

    #사과가 있으면 head이동 tail그대로

    
    
import sys
from collections import deque
# input = sys.stdin.readline
N = int(input()) # 맵크기 n*n
K = int(input())
apple = [tuple(map(int, input().split())) for _ in range(K)]
L = int(input())
moves = {}
for i in range(L):
    X, C = input().split()
    moves[int(X)] = C

dir_ = [(0, 1), (1, 0), (0, -1), (-1, 0)] ## 우, 하, 좌, 상
MAP = [[0] * N for _ in range(N)]
for r, c in apple:
    MAP[r-1][c-1] = 'a'
    
def sol():
    global MAP
    d = 0
    time = 0
    body = deque([(0, 0)])
    nx, ny = 0, 0
    while True:
        nx = nx + dir_[d][0]
        ny = ny + dir_[d][1]
        time += 1
        if nx < 0 or ny < 0 or nx >= N or ny >= N or (nx, ny) in body:
            return time
        if MAP[nx][ny] == 'a':
            MAP[nx][ny] = 0
        else:
            body.popleft()
        body.append((nx, ny))
        
        if time in moves.keys():
            if moves[time] == 'L':
                d = (d - 1)
            else:
                d = (d + 1)
            if d >= 4:
                d -= 4
            if d < 0 :
                d += 4
            
sol()